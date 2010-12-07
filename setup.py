#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import pyidml

setup(
    name='pyidml',
    version=pyidml.__version__,
    description='A Python IDML library',
    author=pyidml.__author__,
    author_email=pyidml.__contact__,
    url=pyidml.__homepage__,
    packages=['pyidml'],
    test_suite='nose.collector',
)
