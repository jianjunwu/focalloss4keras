#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2020/06/24 10:35:57
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
from setuptools import setup, find_packages

install_requires = ["tensorflow", "keras"]

setup(
    name="focalloss4keras",
    version="0.0.3",
    python_requires=">=3.5",
    packages=find_packages(),
    author="NICHOLAS WU",
    author_email="nicholas_wu@aliyun.com",
    description="Use less Code implement focal loss based on keras . Both suport tf.keras 2.0 and keras.",
    long_description="Use less Code implement focal loss based on keras . Both suport tf.keras 2.0 and keras. See https://github.com/jianjunwu/focalloss4keras for complete user guide.",
    url="https://github.com/jianjunwu/focalloss4keras",
    install_requires=install_requires,
    license="MIT",
)
