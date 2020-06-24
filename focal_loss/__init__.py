#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2020/06/24 09:14:46
@Author  :   nicholas wu 
@Version :   1.0
@Contact :   nicholas_wu@aliyun.com
@License :    
@Desc    :   None
'''
import tensorflow as tf
from focal_loss.backend import keras, K

__version__ = '0.0.2'


class FocalLoss(keras.losses.Loss):
    def __init__(self,
                 alpha=[0.25, 0.75],
                 gamma=2,
                 reduction=keras.losses.Reduction.AUTO,
                 name='focal_loss'):
        super(FocalLoss, self).__init__(
            name=name,
            reduction=reduction)
        self.alpha = alpha
        self.gamma = gamma

    def call(self, y_true, y_pred):
        assert len(y_true.shape) == 2, "y_true must be one_hot."
        assert y_true.shape[1] == len(self.alpha), "list alpha length must equal class number."
        y_true = tf.convert_to_tensor(y_true, dtype=tf.float32)
        y_pred = tf.convert_to_tensor(y_pred, dtype=tf.float32)
        pt = K.softmax(y_pred, axis=1)
        cross_entropy = K.abs(y_true * K.log(pt))
        loss = self.alpha * K.pow(1 - pt, self.gamma) * cross_entropy
        return loss
