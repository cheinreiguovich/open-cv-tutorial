import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])
print(x, y, cv2.add(x,y), x + y)

imgOMJ = cv2.imread('omj.jpg')
imgLogo = cv2.imread('opencv-logo-white.png')

rowLogo, colLogo, chnLogo = imgLogo.shape
roi = imgOMJ[0:rowLogo, 0:colLogo]

imgLogoGray = cv2.cvtColor(imgLogo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgLogoGray, 10, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

imgOMJ_bg = cv2.bitwise_and(roi, roi, mask = maskInv)
imgLogo_fg = cv2.bitwise_and(imgLogo, imgLogo, mask = mask)

dst = cv2.add(imgOMJ_bg, imgLogo_fg)
dst = cv2.addWeighted(imgOMJ_bg, 0.5, imgLogo_fg, 0.5, 0)
imgOMJ[0:rowLogo, 0:colLogo] = dst

output = imgOMJ
print(output.shape)
cv2.imshow('Result', output)
cv2.waitKey(0)
cv2.destroyAllWindows()