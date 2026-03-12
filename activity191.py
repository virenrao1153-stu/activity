import cv2
import numpy as np

image = cv2.imread("input.jpg")

h, w = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 15, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))

brightness = 50
bright = cv2.convertScaleAbs(rotated, beta=brightness)

x = int(w * 0.25)
y = int(h * 0.25)
crop = bright[y:y + int(h * 0.5), x:x + int(w * 0.5)]

cv2.imshow("Original", image)
cv2.imshow("Rotated", rotated)
cv2.imshow("Bright", bright)
cv2.imshow("Cropped", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread("input.jpg")

h, w = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 15, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))

brightness = 50
bright = cv2.convertScaleAbs(rotated, beta=brightness)

x = int(w * 0.25)
y = int(h * 0.25)
crop = bright[y:y + int(h * 0.5), x:x + int(w * 0.5)]

cv2.imshow("Original", image)
cv2.imshow("Rotated", rotated)
cv2.imshow("Bright", bright)
cv2.imshow("Cropped", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
