#!/usr/bin/env python

from distutils.core import setup

setup(name='custom_text_test_runner',
      version='1.0',
      description='Python Custom Text Test Runner',
      author='Abtin Gramian',
      author_email='abtin.gramian@gmail.com',
      url='https://github.com/agramian/custom-text-test-runner',
      packages=['custom_text_test_runner'],
      install_requires=['table_printer'],
      dependency_links=['git+git://github.com/agramian/table-printer.git']
     )
