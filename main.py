import numpy as np
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret, frame = cv2.threshold(frame, 80, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# the following is necessary on the mac,
# maybe not on other platforms:
cv2.waitKey(1)
