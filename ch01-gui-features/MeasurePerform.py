import numpy as np
import cv2

cv2.setUseOptimized(True)
print('Optimized status:',cv2.useOptimized())

img = cv2.imread('omj.jpg')
e1 = cv2.getTickCount()

rng = range(5,49,2)
for i in rng:
    img = cv2.medianBlur(img, i)
e2 = cv2.getTickCount()
t = (e2-e1)/cv2.getTickFrequency()
print('Elapsed time:',t,'s')

'''
cv2.useOptimized()
cv2.setUseOptimized(False)
'''

'''
cv2.imshow("figure", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''