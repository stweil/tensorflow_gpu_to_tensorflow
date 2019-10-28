# -*- coding: utf-8 -*-
"""
Dummy Python package for tensorflow-gpu
"""

import codecs
import setuptools

setuptools.setup(
    name='tensorflow_gpu',
    version='1.14',
    description='dummy for tensorflow-gpu',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Stefan Weil',
    author_email='sw@weilnetz.de',
    url='https://github.com/stweil/tensorflow_gpu_to_tensorflow',
    license='Apache License 2.0',
    install_requires=[
        'tensorflow'
    ],
)
