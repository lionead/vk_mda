#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: lionead
:license: Apache License, Version 2.0, see LICENSE file

:copyright: (c) 2020 lionead
"""


version = '11.9.2'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vk_mda',
    version=version,

    author='lionead',
    author_email='lionia058@gmail.com',

    description=(
        u'Python модуль для написания скриптов для социальной сети '
        u'Вконтакте (vk.com) (API wrapper)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/lionead/vk_mda',
    download_url='https://github.com/lionead/vk_mda/archive/master.zip',

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['vk_mda', 'jconfig'],
    install_requires=['requests', 'enum34;python_version<"3.4"', 'six'],
    extras_require={
        'vkstreaming': ['websocket-client'],
        'vkaudio': ['beautifulsoup4'],
    },

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
