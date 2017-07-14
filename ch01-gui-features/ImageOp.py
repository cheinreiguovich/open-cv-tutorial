import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load
img = cv2.imread('omj.jpg')

# Pixel
px1 = img[100, 100]
px1B = img[100, 100, 0]
px1G = img[100, 100, 1]
px1R = img[100, 100, 2]
img[100, 100, 0] = 255
img[100, 100, 1] = 127
img[100, 100, 2] = 63
print(img[100, 100])

# Properties
px2B = img.item(200, 200, 0)
img.itemset((200, 200, 0), 255)
print(img.item(200, 200, 0))
print('Shape: ', img.shape, '\nSize: ', img.size, '\nDType: ', img.dtype)

# ROI
title = img[190:240, 300:360]
img[0: 50, 0: 60] = title

# Split & Merge
b, g, r = cv2.split(img) # b = img[:,:,0]; g = img[:,:,1]; r = img[:,:,2]
img = cv2.merge((b, g, r))

img2 = cv2.imread('opencv-logo-white.png')
BLUE = [255, 0, 0] # BGR order
replicate = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = BLUE)

plt.subplot(231), plt.imshow(img2), plt.title('Original')
plt.subplot(232), plt.imshow(replicate), plt.title('Replicate')
plt.subplot(233), plt.imshow(reflect), plt.title('Reflect')
plt.subplot(234), plt.imshow(reflect101), plt.title('Reflect101')
plt.subplot(235), plt.imshow(wrap), plt.title('Wrap')
plt.subplot(236), plt.imshow(constant), plt.title('Constant')
plt.show()