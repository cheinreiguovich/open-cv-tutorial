import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('omj.jpg', 1)

'''
nameWindow = 'Figure'
cv2.namedWindow(nameWindow, cv2.WINDOW_NORMAL)
cv2.imshow(nameWindow, img)
wk = cv2.waitKey(0 * 1000)  # ms
if wk == 27:  # ESC
    cv2.destroyAllWindows()
elif wk == ord('s'):  # s
    cv2.imwrite('ImgWrite.png', img)
    cv2.destroyAllWindows()
'''

'''
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
'''

'''
x = np.arange(0, 2 * 3.14, 1e-2)
y = np.sin(x)
plt.plot(x, y)
plt.show()
'''

img1 = cv2.imread('omj.jpg')
b,g,r = cv2.split(img1)
#img2 = cv2.merge([r,g,b])
#img2 = img1[:,:,::-1]
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.subplot(121); plt.imshow(img1)
plt.subplot(122); plt.imshow(img2)
plt.show()

cv2.imshow('BGR image', img1)
cv2.imshow('RGB image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()