# import os
# import logging
# import re
# from urllib.request import urlretrieve

# from .mod_pdfminer.layout import LAParams
# from .mod_pdfminer.high_level import extract_text

# logging.getLogger("mod_pdfminer").setLevel(logging.WARNING)


# def text_extractor(path, fname):
#     pdf = path + fname + '.pdf'
#     if not pdf:
#         raise ValueError("Must provide files to work upon!")

#     raw_text = extract_text(pdf, laparams=LAParams())
#     return raw_text


# def slugify(obj):
#     # Remove special characters from object title
#     filename = '_'.join(re.findall(r'\w+', obj.get('title', 'UNTITLED')))
#     return filename


# def download(obj, dirpath):

#     if not obj.get('pdf_url', ''):
#         print('Object has no PDF URL.')
#         return

#     url = obj['pdf_url']
#     name = slugify(obj)
#     path = dirpath + name + '.pdf'
#     urlretrieve(url, path)
#     return name


# def extract(obj):
#     """This Function downloads the selected pdf and converts it into a txt file and
#     removes the downloaded pdf"""

#     output_dir = os.getcwd() + '/data/'
#     pdf_name = download(obj, output_dir)

#     raw_text = text_extractor(output_dir, pdf_name)
#     logging.info('PDF to Text Extraction Complete')
#     pdf_path = output_dir + pdf_name + '.pdf'
#     os.remove(pdf_path)
#     logging.info('PDF File Removed')

#     return raw_text

# For Importing relative modules
# import os.path
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
