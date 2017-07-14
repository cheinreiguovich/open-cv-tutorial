import cv2
import numpy as np

'''
cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lb_blue = np.array([100, 10, 10])
    ub_blue = np.array([150, 255, 255])

    mask = cv2.inRange(hsv, lb_blue, ub_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)
    if cv2.waitKey(1) == 32:
        break
cv2.destroyAllWindows()
'''

img = cv2.imread('opencv-logo-white.png')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

bgr_BLUE = np.uint8([[[255, 0, 0]]])
bgr_GREEN = np.uint8([[[0, 255, 0]]])
bgr_RED = np.uint8([[[0, 0, 255]]])

hsv_BLUE = cv2.cvtColor(bgr_BLUE, cv2.COLOR_BGR2HSV)
hsv_GREEN = cv2.cvtColor(bgr_GREEN, cv2.COLOR_BGR2HSV)
hsv_RED = cv2.cvtColor(bgr_RED, cv2.COLOR_BGR2HSV)

lb_BLUE = np.array([hsv_BLUE[0][0][0]-10, 100, 100])
ub_BLUE = np.array([hsv_BLUE[0][0][0]+10, 255, 255])
lb_GREEN = np.array([hsv_GREEN[0][0][0]-10, 100, 100])
ub_GREEN = np.array([hsv_GREEN[0][0][0]+10, 255, 255])
lb_RED = np.array([hsv_RED[0][0][0]-10, 100, 100])
ub_RED = np.array([hsv_RED[0][0][0]+10, 255, 255])

mask_BLUE = cv2.inRange(hsv_img, lb_BLUE, ub_BLUE)
mask_GREEN = cv2.inRange(hsv_img, lb_GREEN, ub_GREEN)
mask_RED = cv2.inRange(hsv_img, lb_RED, ub_RED)

res_BLUE = cv2.bitwise_and(img, img, mask = mask_BLUE)
res_GREEN = cv2.bitwise_and(img, img, mask = mask_GREEN)
res_RED = cv2.bitwise_and(img, img, mask = mask_RED)

cv2.imshow('Result BLUE', res_BLUE)
cv2.imshow('Result GREEN', res_GREEN)
cv2.imshow('Result RED', res_RED)
cv2.waitKey(0)
cv2.destroyAllWindows()