# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import re

package_name = 'falcon_vue'

root_dir = path.abspath(path.dirname(__file__))

REQUIRES = ['falcon>=1.4.0']


with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(
        r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)
    license = re.search(
        r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)
    author = re.search(
        r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)
    author_email = re.search(
        r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text
    ).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version=version,
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
    author=author,
    author_email=author_email,
    description="An unladen web framework for building APIs and app backends.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=license,
    keywords="falcon vue falcon-vue falcon_vue",
    url=url,
    python_requires='>=3.4, !=2.7.*',
    install_requires=REQUIRES,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
)
