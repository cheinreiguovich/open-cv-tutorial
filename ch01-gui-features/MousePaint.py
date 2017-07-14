import numpy as np
import cv2

'''
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
'''


def draw_circle(event, x, y, flags, param):
    # Double-click callback function
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


def draw_adv(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # Left mouse down/move/up callback functions
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = 1
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == 1:
                cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 5, cv2.LINE_AA)
            elif mode == 2:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            elif mode == 3:
                # v = np.array([x,y]) - np.array([ix,iy])
                # r = int(np.linalg.norm(v)/2)
                cv2.circle(img,(x, y), 20, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = 0
        if mode == 1:
            cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 5, cv2.LINE_AA)
        elif mode == 2:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        elif mode == 3:
            cv2.circle(img,(x, y), 20, (0, 0, 255), -1)


# Initialization
drawing = 0
mode = 1
ix, iy = -1, -1

# Setup background
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Figure')
cv2.setMouseCallback('Figure', draw_adv)

# Drawing
while (1):
    cv2.imshow('Figure', img)
    key = cv2.waitKey(1)
    if key == 32:
        mode += 1
        if mode > 3:
            mode = 1
        if mode == 1:
            print('Mode: Line')
        elif mode == 2:
            print('Mode: Rectangular')
        elif mode == 3:
            print('Mode: Circle')
    elif key == 27:
        break

# Saving
cv2.imshow('Figure', img)
cv2.imwrite('MousePaint.jpg', img)
cv2.destroyAllWindows()
