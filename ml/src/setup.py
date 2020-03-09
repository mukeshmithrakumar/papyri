# Copyright 2020, Mukesh Mithrakumar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Papyri

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup
import os

version = {}
base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, "src", "version.py")) as fp:
    exec(fp.read(), version)


project_name = 'papyri'

REQUIRED_PACKAGES = [
    'feedparser == 5.2.1',
    'pdfminer3 == 2018.12.03.0'
]

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name=project_name,
    version=version['0.1.0-dev'],
    description='....................',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mukesh Mithrakumar',
    author_email='mukesh@mukeshmithrakumar.com',
    url='https://github.com/mukeshmithrakumar/papyri',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    project_urls={
        'Source': 'https://github.com/mukeshmithrakumar/papyri'
    },
    license='Apache 2.0',
    keywords=('ocr')
)
