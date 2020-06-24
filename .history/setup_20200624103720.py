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

install_requires = ["dill", "pandarallel"]

setup(
    name="focal_loss",
    version="0.0.1",
    python_requires=">=3.5",
    packages=find_packages(),
    author="NICHOLAS WU",
    author_email="nicholas_wu@aliyun.com",
    description="An easy to use library to speed up computation (by parallelizing on multi CPUs).",
    long_description="See https://github.com/jianjunwu/parallel-map for complete user guide.",
    url="https://github.com/jianjunwu/parallel-map",
    install_requires=install_requires,
    license="MIT",
)
