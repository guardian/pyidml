#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pyidml',
    version='0.3-dev',
    description='A Python IDML library',
    url='https://github.com/guardian/pyidml',
    packages=find_packages(exclude=['tests']),
    test_suite='nose.collector',
)
