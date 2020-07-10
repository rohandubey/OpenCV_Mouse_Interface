# matplotlib order rgb.. opencv bgr
import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread('flower.jpeg')
print(type(img))
img_fix = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_fix)
plt.show()



cv2.imshow('qwq',img)
cv2.waitKey()
