import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img=Image.open("flower.jpeg")

# img =img.rotate(-90)
img=np.asarray(img)
plt.imshow(img)
print(type(img))
plt.show()
