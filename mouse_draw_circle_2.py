import numpy as np
import matplotlib.pyplot as plt
import cv2
def draw_circle(event,x,y,flags,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),70,(35,69,78),-1)
    if event ==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,69,78),-1)
cv2.namedWindow(winname='Drawing')

cv2.setMouseCallback('Drawing',draw_circle)

img = np.zeros((512,512,3),np.int8)
while True:
    cv2.imshow('Drawing',img)

    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
