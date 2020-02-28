from __future__ import print_function

import logging
import time
from urllib.parse import urlencode

import feedparser


class Search(object):
    """Class to search and download abstracts from the arXiv.

    Code from https://github.com/lukasschwab/arxiv.py

    Args:
        object ([type]): [description]
    """

    root_url = 'http://export.arxiv.org/api/'
    prune_keys = [
        'updated_parsed',
        'published_parsed',
        'arxiv_primary_category',
        'summary_detail',
        'author',
        'author_detail',
        'links',
        'guidislink',
        'title_detail',
        'tags',
        'id'
    ]

    def __init__(self, query=None, id_list=None, max_results=None, start=0, sort_by=None,
                 sort_order=None, max_chunk_results=None, time_sleep=3, prune=True):

        self.query = query
        self.id_list = id_list
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.max_chunk_results = max_chunk_results
        self.time_sleep = time_sleep
        self.prune = prune
        self.max_results = max_results
        self.start = start

        if not self.max_results:
            logging.info('max_results defaulting to 1.')
            self.max_results = 1

    def _get_url(self, start=0, max_results=None):

        url_args = urlencode(
            {
                'search_query': self.query,
                'id_list': self.id_list,
                'start': start,
                'max_results': max_results,
                'sortBy': self.sort_by,
                'sortOrder': self.sort_order
            }
        )

        return self.root_url + 'query?' + url_args

    def _parse(self, url):
        """Downloads the data provided by the REST endpoint given in the url."""

        result = feedparser.parse(url)

        if result.get('status') != 200:
            logging.error('HTTP Error {} in query'.format(result.get('status', 'no status')))
            return []
        return result['entries']

    def _prune_result(self, result):
        """Deletes some of the keys from the downloaded result."""

        for key in self.prune_keys:
            try:
                del result['key']
            except KeyError:
                pass
        return result

    def _process_result(self, result):

        # Useful to have for download automation
        result['pdf_url'] = None
        for link in result['links']:
            if 'title' in link and link['title'] == 'pdf':
                result['pdf_url'] = link['href']

        result['affiliation'] = result.pop('arxiv_affiliation', 'None')
        result['arxiv_url'] = result.pop('link')
        result['title'] = result['title'].rstrip('\n')
        result['summary'] = result['summary'].rstrip('\n')
        result['authors'] = [d['name'] for d in result['authors']]

        if 'arxiv_comment' in result:
            result['arxiv_comment'] = result['arxiv_comment'].rstrip('\n')
        else:
            result['arxiv_comment'] = None

        if 'arxiv_journal_ref' in result:
            result['journal_reference'] = result.pop('arxiv_journal_ref')
        else:
            result['journal_reference'] = None

        if 'arxiv_doi' in result:
            result['doi'] = result.pop('arxiv_doi')
        else:
            result['doi'] = None

        if self.prune:
            result = self._prune_result(result)

        return result

    def _get_next(self):

        n_left = self.max_results
        start = self.start

        while n_left > 0:
            if n_left < self.max_results:
                logging.info('...play nice on the arXiv and sleep a bit...')
                time.sleep(self.time_sleep)
            logging.info('Fetch from arxiv ({} results left to download)'.format(n_left))
            url = self._get_url(
                start=start,
                max_results=min(n_left, self.max_chunk_results)
            )
            results = self._parse(url)

            # Update the entries left to download
            n_fetched = len(results)
            logging.info('Received {} entries'.format(n_fetched))

            if n_fetched == 0:
                logging.info('No more entries left to fetch')
                logging.info('Fetching finished.')
                break

            # Update the number of results left to download
            n_left = n_left - n_fetched
            start = start + n_fetched

            # Process results
            results = [self._process_result(r) for r in results if r.get('title', None)]

            yield results

    def download(self, iterative=False):
        """Triggers the download of the result of the given search query.

        Args:
            iterative (bool, optional): [description]. Defaults to False.
        """
        logging.info('Start Downloading')
        if iterative:
            logging.info('Build iterator')

            def iterator():
                logging.info('Start iterating')
                for result in self._get_next():
                    for entry in result:
                        yield entry
            return iterator

        else:
            results = list()
            for result in self._get_next():
                # Only append result if title is not empty
                results = results + result
            return results


def query(query="", id_list=[], prune=True, max_results=None, start=0, sort_by='submittedDate',
          sort_order='descending', max_chunk_results=1, iterative=True):

    if max_results is not None:
        max_chunk_results = max_results
        # iterative = True

    search = Search(
        query=query,
        id_list=','.join(id_list),
        sort_by=sort_by,
        sort_order=sort_order,
        prune=prune,
        max_results=max_results,
        start=start,
        max_chunk_results=max_chunk_results
    )

    return search.download(iterative=iterative)


# if __name__ == '__main__':
#     result = query(query='Deep Nearest')
#     for paper in result():
#         print(paper['title'], paper['pdf_url'])
#         download(paper)
