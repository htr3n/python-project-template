# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-project-template',
    version='0.0.1',
    description='Python project template',
    long_description=readme,
    author='Huy Tran',
    author_email='me@my-domain.com',
    url='https://github.com/htr3n/python-project-template',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
