#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join

here = dirname(__file__)

setup(name='traiding-one',
      version='0.1',
      description='auto traiding bot',
      long_description=open(join(here, 'README.md')).read(),
      author='Jan Matuszewski',
      author_email='matuszewski.jan@gmail.com',
      url='',
      install_requires=[
          'requests'
      ]
     )

print "\n**** \nImportant!!!\nCopy settings.py.example to settings.py and edit before starting the bot.\n****"
