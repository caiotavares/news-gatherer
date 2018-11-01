#!/usr/bin/env python
from os.path import join
from setuptools import setup, find_packages

def requirements_from_pip():
    with open('requirements.txt', 'r') as pip:
        return [l.strip() for l in pip if not l.startswith('#') and l.strip()]

setup(
    name='news-gatherer',
    description='News gatherer for The Guardian',
    url='https://github.com/caiotavares/news-gatherer',
    author='CT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    version='1.0',
    install_requires=requirements_from_pip(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Programming Language :: Python :: 3.6']
)