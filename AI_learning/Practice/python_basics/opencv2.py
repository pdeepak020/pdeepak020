import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys

np.random.seed(9)
x = np.random.randint(1,20,5)

# Image filename (place image next to this script or set an absolute path)
filename = 'WhatsApp Image 2025-05-20 at 09.32.07_4bfcd1b4.jpg'
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, filename)

if not os.path.exists(filepath):
	print(f"ERROR: image file not found: {filepath}")
	print("Put the image file next to the script or update `filename` to a correct path.")
	sys.exit(1)

image = cv2.imread(filepath)
if image is None:
	print(f"ERROR: cv2.imread failed to load the image at {filepath}")
	sys.exit(1)

# Convert BGR to RGB
try:
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
except cv2.error as e:
	print("ERROR: cvtColor failed:", e)
	sys.exit(1)

plt.imshow(image)
plt.show()
