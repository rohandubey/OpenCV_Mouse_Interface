import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img=Image.open("flower.jpeg")
print(type(img))
# img =img.rotate(-90)
img=np.asarray(img)
plt.imshow(img)
img_copy=img.copy()
plt.imshow(img_copy[:,:,0])
plt.imshow(img_copy[:,:,0],cmap='gray')
img_copy[:,:,2]=img_copy[:,:,1]
img_copy[:,:,0]=img_copy[:,:,1]
plt.imshow(img_copy)


plt.show()
