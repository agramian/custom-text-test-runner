#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='custom_text_test_runner',
      version='0.1.2',
      description='Python Custom Text Test Runner',
      long_description=read_md('README.md'),
      author='Abtin Gramian',
      author_email='abtin.gramian@gmail.com',
      url='https://github.com/agramian/custom-text-test-runner',
      packages=['custom_text_test_runner'],
      install_requires=['table_printer'],
      download_url = 'https://github.com/agramian/custom-text-test-runner/tarball/v0.1.2',
      keywords = ['unittest', 'custom', 'test', 'runner', 'result', 'json'],
      classifiers = [],
     )
