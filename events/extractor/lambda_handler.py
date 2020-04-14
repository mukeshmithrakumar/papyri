import re
import boto3
import unicodedata
from urllib.error import URLError
from urllib.request import urlretrieve

from pdfminer3.high_level import extract_text


# TODO: I should move the clean into a different Lambda function and do serialized cleaning rather than batch with 512 words
class Clean:
    def join_text(self, raw_text):
        """Function to Join paragraphs together"""
        joined_text = []
        line = ''
        for i in range(len(raw_text)):
            if (len(raw_text[i]) > 1) and (raw_text[i][-1] == '\n'):
                line += raw_text[i]
            if (raw_text[i] == '\n'):
                joined_text.append(line)
                line = ''
        return joined_text

    def remove_non_ascii(self, word):
        """Remove non-ASCII characters from list of tokenized words"""
        return unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    def remove_punctuation(self, word):
        """Remove punctuation from list of tokenized words"""
        return re.sub(r'[^\w\s]', '', word)

    def clean_text(self, text_path):
        with open(text_path, 'r', encoding='utf-8') as file:
            _text = file.readlines()
        file.close()

        # Call the function to join the paragraph texts together.
        raw_text = self.join_text(_text)

        for line in range(len(raw_text)):

            # Remove numbers
            raw_text[line] = re.sub(r'[0-9]', ' ', raw_text[line])

            # Remove non ascii characters
            raw_text[line] = ' '.join(map(self.remove_non_ascii, raw_text[line].split()))

            # Remove punctuation
            raw_text[line] = ' '.join(map(self.remove_punctuation, raw_text[line].split()))

            # Remove extra whitespace
            raw_text[line] = re.sub(r'\s+', ' ', raw_text[line])

            # Remove extra whitespace
            raw_text[line] = raw_text[line].lstrip()

        return list(filter(None, raw_text))


def slugify(obj):
    # Remove special characters from object title
    filename = '_'.join(re.findall(r'\w+', obj.get('title', 'UNTITLED')))
    return filename


# !Note that my version of extract_text didn't work until I added the LAparams import in the high_level.py file manually
class Extract:
    def extracting_text(self, path, fname):
        pdf = path + fname + '.pdf'
        if not pdf:
            raise ValueError("Must provide files to work upon!")

        return extract_text(pdf)

    def slugify(self, obj):
        # Remove special characters from object title
        filename = '_'.join(re.findall(r'\w+', obj.get('title', 'UNTITLED')))
        return filename

    def download_pdf(self, url, dirpath, name):
        """Function to download PDF and store in AWS bucket"""

        pdf_url = url.replace('abs', 'pdf')
        path = dirpath + name + '.pdf'
        try:
            urlretrieve(pdf_url, path)
        except URLError as e:
            print(e)
        return True

    def text_extract(self, obj):
        """This Function downloads the selected pdf and converts it into a txt file and
        removes the downloaded pdf"""

        output_dir = '/tmp/'
        pdf_name = self.slugify(obj)

        # Download pdf
        self.download_pdf(obj.get('url'), output_dir, pdf_name)

        # Extract pdf
        raw_text = self.extracting_text(output_dir, pdf_name)
        return raw_text


def lambda_handler(event, context):
    raw_text = Extract().text_extract(event)

    # Save Cleaned Text Data
    output_dir = '/tmp/'
    raw_text_path = output_dir + "raw_text.txt"

    with open(raw_text_path, 'w', encoding='utf-8') as fp:
        fp.write(raw_text)
    fp.close()

    clean_text_list = Clean().clean_text(raw_text_path)

    # Save Cleaned Text Data
    paper_name = slugify(event)

    paper_text = output_dir + paper_name + '.txt'
    with open(paper_text, "w", encoding='utf-8') as file:
        file.writelines("%s\n" % line for line in clean_text_list)
    file.close()

    # Move file to S3 bucket
    s3 = boto3.resource('s3')

    key = paper_name + '.txt'
    bname = "papyricleantext"
    s3.Bucket(bname).upload_file(paper_text, key)

    # return path to S3 bucket
    return {'key': key,
            'bucket_name': bname}
