import os
import logging
import re
from urllib.request import urlretrieve

from pdfminer3.high_level import extract_text_to_fp
from pdfminer3.layout import LAParams

logging.getLogger("pdfminer3").setLevel(logging.WARNING)


def extract_text(path, fname):
    pdf = path + fname + '.pdf'
    if not pdf:
        raise ValueError("Must provide files to work upon!")

    laparams = LAParams()
    for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
        paramv = locals().get(param, None)
        if paramv is not None:
            setattr(laparams, param, paramv)

    text = path + fname + '.txt'
    outfp = open(text, "wb")

    with open(pdf, 'rb') as fp:
        extract_text_to_fp(fp, **locals())
    outfp.close()


def slugify(obj):
    # Remove special characters from object title
    filename = '_'.join(re.findall(r'\w+', obj.get('title', 'UNTITLED')))
    return filename


def download(obj, dirpath):

    if not obj.get('pdf_url', ''):
        print('Object has no PDF URL.')
        return

    url = obj['pdf_url']
    name = slugify(obj)
    path = dirpath + name + '.pdf'
    urlretrieve(url, path)
    return name


def convert(obj):
    """This Function downloads the selected pdf and converts it into a txt file and
    removes the downloaded pdf"""

    output_dir = os.getcwd() + '/data/'

    pdf_name = download(obj, output_dir)

    extract_text(output_dir, pdf_name)
    logging.info('PDF to Text Conversion Complete')
    pdf_path = output_dir + pdf_name + '.pdf'
    text_path = output_dir + pdf_name + '.txt'
    os.remove(pdf_path)
    logging.info('PDF File Removed')

    return text_path
