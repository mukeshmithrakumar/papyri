
import logging
import os

from modules.text_extractor import pdf2txt
from modules.text_extractor import text_cleaner


def preprocess(obj):
    # Call from Flask to run pdf2text.py
    text_path = pdf2txt.convert(obj)

    # Start Cleaning Raw Data
    cleaned_raw_text = text_cleaner.cleaner(text_path)
    logging.info('Finished Cleaning Raw data')
    os.remove(text_path)
    logging.info('Removed Raw data')

    # Save Cleaned Text Data
    output_dir = os.getcwd() + '/data/'
    text = output_dir + obj['title'] + '.txt'
    with open(text, "w") as file:
        file.writelines("%s\n" % line for line in cleaned_raw_text)
    file.close()
    logging.info('Wrote Cleaned Data to file')


def main():
    # logger = logging.getLogger(__name__)
    logging.basicConfig(filename='src.log', level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(process)d: %(name)s: %(message)s',
                        datefmt='%d-%m-%Y %H:%M:%S')

    logging.info('Started')

    # This will be replaced by the request from Flask
    title = 'Deep Reinforcement Learning for Intelligent Reflecting Surfaces'
    pdf_url = 'http://arxiv.org/pdf/2002.11101v1'
    obj = {'pdf_url': pdf_url, 'title': title}

    # Start Text Extraction and Preprocessing
    preprocess(obj)


if __name__ == '__main__':
    main()
