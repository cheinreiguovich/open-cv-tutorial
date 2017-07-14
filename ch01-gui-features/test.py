import numpy as np
import cv2

img = cv2.imread('opencv-logo-white.png')
rowImg, colImg, chnImg = img.shape
mask = cv2.imread('omj.jpg', 0)
roiMask = mask[0:rowImg, 0:colImg]
res = cv2.bitwise_and(img,img, mask = roiMask)

cv2.imshow('test',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
