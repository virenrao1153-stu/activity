import cv2

image = cv2.imread("input.jpg")

small = cv2.resize(image, (200, 200))
medium = cv2.resize(image, (400, 400))
large = cv2.resize(image, (600, 600))

cv2.imshow("Original", image)
cv2.imshow("Small", small)
cv2.imshow("Medium", medium)
cv2.imshow("Large", large)

cv2.imwrite("small.jpg", small)
cv2.imwrite("medium.jpg", medium)
cv2.imwrite("large.jpg", large)

cv2.waitKey(0)
cv2.destroyAllWindows()