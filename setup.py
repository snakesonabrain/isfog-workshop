#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

# load the README file and use it as the long_description for PyPI
def readme():
    with open('README.md', 'r') as f:
        return f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
      name='isfog-workshop',
      version='1.0',
      description='Notebooks for the ISFOG pre-conference workshop on data science',
      long_description=readme(),
      url='',
      download_url='',
      keywords=['isfog', 'engineering', 'geotechnical'],
      author='Bruno Stuyts',
      author_email='bruno@pro-found.be',
      license='GNU GPL v3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      )