#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from setuptools import setup

setup(
    name='app_home',
    version='1.0',
    license='GNU General Public License v3',
    author='Abhishek N',
    author_email='aanagpurkar@gmail.com',
    description='My first flask app',
    packages=['app_home'],
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)