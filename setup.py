from distutils.core import setup
from setuptools import find_packages
import os

# Optional project description in README.md:
current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''
setup(

# Project name: 
name='Math Integral Finder',

# Packages to include in the distribution: 
packages=find_packages(','),

# Project version number:
version='2.5',

# List a license for the project, eg. MIT License
license='MIT',

# Short description of your library: 
description='Finds integrals of an equation',

# Long description of your library: 
long_description=long_description,
long_description_content_type='text/markdown',

# Your name: 
author='Gabriel Womelsdorf',

# Your email address:
author_email='837297@lcps.org',

# Link to your github repository or website: 
url='https://github.com/Silverwarriorin/MathIntegralFinder',

# Download Link from where the project can be downloaded from:
download_url='',

# List of keywords: 
keywords=[],

# List project dependencies: 
install_requires=[
    'matplotlib',
    'numpy'
],

# https://pypi.org/classifiers/ 
classifiers=[]
)