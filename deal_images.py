#!/usr/bin/env python
# coding=utf-8
import os
import os.path
train_path = "/home/dl/songkai/Fine_Grained_Classification/dataset/images/train/"
for root,dirs,files in os.walk(train_path):
    for name in files:
        print root + '/' + name
        #os.path.join
