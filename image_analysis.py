import cv2
import numpy as np
import matplotlib.pyplot as plt


# Reading an image in
img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)


# Create a windows and show the image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()

# Save an image to a file
cv2.imwrite('testgray.jpg',img)
