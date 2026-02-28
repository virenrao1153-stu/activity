import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))

cropped = image[50:300, 50:300]

brightness = 50
bright = cv2.convertScaleAbs(image, alpha=1, beta=brightness)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(rotated)
plt.title("Rotated")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(cropped)
plt.title("Cropped")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(bright)
plt.title("Brightness Increased")
plt.axis("off")

plt.tight_layout()
plt.show()