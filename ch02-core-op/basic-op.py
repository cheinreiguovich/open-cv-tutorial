#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Basic operations'

__author__ = 'Charles Guo'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_me = cv2.imread('./avatar.jpg')
img_cn = cv2.imread('./china.jpg')

# Merge img
img_mrg = np.zeros((400, 400, 3), np.uint8)
h_mrg, w_mrg = img_mrg[:,:,0].shape

# Cut and resize img_cn
h0_cn = 30
h_cn = 240
w0_cn = 40
w_cn = 320
sh = 0.05
sw = 0.05
roi_cn = img_cn[h0_cn : h0_cn + h_cn, w0_cn : w0_cn + w_cn]
res_cn = cv2.resize(roi_cn, None, fx = sw, fy = sh, interpolation = cv2.INTER_CUBIC)

# Resize img_me
h_me, w_me = img_me[:,:,0].shape
h_me, w_me = min([h_me, w_me]), min([h_me, w_me])
res_me = cv2.resize(img_me, None, fx = h_mrg / h_me, fy = w_mrg / w_me, interpolation = cv2.INTER_CUBIC)

# Merge img
h0_mrg = 0.45 * h_mrg
w0_mrg = 0.55 * w_mrg
img_mrg = res_me
img_mrg[h0_mrg : h0_mrg + sh * h_cn, w0_mrg : w0_mrg + sw * w_cn] = res_cn


#print(img_mrg.shape)

cv2.imshow('image', img_mrg); cv2.waitKey(3 * 1000); cv2.destroyAllWindows()
