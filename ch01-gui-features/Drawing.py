import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 2)
img = cv2.circle(img, (128, 384), 20, (0, 0, 255), -1)
img = cv2.ellipse(img, (256, 256), (100, 50), -30, 0, 180, (255, 255, 0), 4, cv2.LINE_AA)
pnt = np.array([[128, 128], [64, 256], [192, 192], [256, 64]], np.int32)
pnt = pnt.reshape((-1, 1, 2))
img = cv2.polylines(img, [pnt], 1, (0, 255, 255))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello', (16, 511), font, 4, (255, 255, 255), 5, cv2.LINE_AA)
cv2.imshow('Figure', img)
cv2.imwrite('Drawing.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
