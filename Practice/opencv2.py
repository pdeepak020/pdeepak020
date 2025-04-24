import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

np.random.seed(9)
x=np.random.randint(1,20,5)
image = cv2.imread('DSC_0993.JPG')
# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
