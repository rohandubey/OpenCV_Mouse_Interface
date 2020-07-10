import numpy as np
import matplotlib.pyplot as plt
import cv2
# Variables
# True whn mouse button is down
# False whn mouse button is up
drawing = False
ex =-1
ey =-1
# Function
# x,y, falgs, param are automatically taken from opencv

def draw_circle(event,x,y,flags,params):
    global ex,ey,drawing

    if event ==cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ex,ey=x,y

    elif event == cv2.EVENT_MOUSEMOVE:

        if drawing == True:
            cv2.rectangle(img,(ex,ey),(x,y),(255,0,0),-1)

    elif event==cv2.EVENT_LBUTTONUP:
        drawing =False
        cv2.rectangle(img,(ex,ey),(x,y),(255,0,0),-1)
        preim = img
cv2.namedWindow(winname='Drawing')

cv2.setMouseCallback('Drawing',draw_circle)

img = np.zeros((512,512,3),np.int8)
while True:
    cv2.imshow('Drawing',img)

    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
