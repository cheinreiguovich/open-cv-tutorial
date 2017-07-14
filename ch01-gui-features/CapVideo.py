import numpy as np
import cv2


'''
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera is not open!')
    cap.open()
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cap.set(3, 320); cap.set(4, 240)
    cv2.imshow('frame', frame)
    # cv2.imshow('frame', gray)
    # print(cap.get(3),'x',cap.get(4))
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
'''


cap = cv2.VideoCapture(0)
fourCC = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
out = cv2.VideoWriter('output.avi',fourCC, fps, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame,1)
        #out.write(frame)
        cv2.imshow('Recording...', frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

