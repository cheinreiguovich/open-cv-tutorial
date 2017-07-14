import numpy as np
import cv2

def nothing(x):
    pass

def funDrawing(event, x, y, flags, param):
    global drawing, mode, initX, initY
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = 1
        initX, initY = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            pass
        else:
            pass
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = 0
        cv2.line(img, (initX, initY), (x, y), (b, g, r), tn)
barName1 = 'R'
barName2 = 'G'
barName3 = 'B'
barName4 = 'Thickness'
winName1 = 'Palette Painting'

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(winName1)
cv2.setMouseCallback(winName1, funDrawing)
cv2.createTrackbar(barName1, winName1, 0, 255, nothing)
cv2.createTrackbar(barName2, winName1, 0, 255, nothing)
cv2.createTrackbar(barName3, winName1, 0, 255, nothing)
cv2.createTrackbar(barName4, winName1, 1, 10, nothing)
drawing, mode = 0, 0
initX, initY = -1, -1

while(1):
    cv2.imshow(winName1, img)
    r = cv2.getTrackbarPos(barName1, winName1)
    g = cv2.getTrackbarPos(barName2, winName1)
    b = cv2.getTrackbarPos(barName3, winName1)
    tn = cv2.getTrackbarPos(barName4, winName1)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.imwrite('PalettePaint.jpg', img)
cv2.destroyAllWindows()