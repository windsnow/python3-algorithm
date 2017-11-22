# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:58:49 2017

@author: HuYao
"""

import cv2

print(cv2.__version__)
image = cv2.imread('E:\\cat.0.jpg')
cv2.imshow('im', image)
cv2.waitKey()