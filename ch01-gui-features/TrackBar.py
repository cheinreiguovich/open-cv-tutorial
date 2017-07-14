import numpy as np
import cv2


def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Palette')

cv2.createTrackbar('R', 'Palette', 0, 255, nothing)
cv2.createTrackbar('G', 'Palette', 0, 255, nothing)
cv2.createTrackbar('B', 'Palette', 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Palette', 0, 1, nothing)

while (1):
    cv2.imshow('Palette', img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    r = cv2.getTrackbarPos('R', 'Palette')
    g = cv2.getTrackbarPos('G', 'Palette')
    b = cv2.getTrackbarPos('B', 'Palette')
    s = cv2.getTrackbarPos(switch, 'Palette')
    if s:
        img[:] = [b, g, r]
    else:
        img[:] = 0
cv2.destroyAllWindows()
