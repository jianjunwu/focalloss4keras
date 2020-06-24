#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   backend.py
@Time    :   2020/06/24 09:21:29
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
import os
import sys
from distutils.util import strtobool

is_tf_keras = strtobool(os.environ.get('TF_KERAS', '0'))
if is_tf_keras:
    import tensorflow.keras as keras
    import tensorflow.keras.backend as K
    sys.modules['keras'] = keras
else:
    import keras
    import keras.backend as K
