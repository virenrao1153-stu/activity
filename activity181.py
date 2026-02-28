import cv2
import numpy as np

image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("Controls")

cv2.createTrackbar("Canny Th1", "Controls", 50, 500, lambda x: None)
cv2.createTrackbar("Canny Th2", "Controls", 150, 500, lambda x: None)
cv2.createTrackbar("Gaussian Kernel", "Controls", 1, 20, lambda x: None)
cv2.createTrackbar("Median Kernel", "Controls", 1, 20, lambda x: None)

while True:
    th1 = cv2.getTrackbarPos("Canny Th1", "Controls")
    th2 = cv2.getTrackbarPos("Canny Th2", "Controls")
    gk = cv2.getTrackbarPos("Gaussian Kernel", "Controls")
    mk = cv2.getTrackbarPos("Median Kernel", "Controls")

    if gk % 2 == 0:
        gk += 1
    if mk % 2 == 0:
        mk += 1
    if gk <= 1:
        gk = 1
    if mk <= 1:
        mk = 1

    gaussian = cv2.GaussianBlur(gray, (gk, gk), 0)
    median = cv2.medianBlur(gray, mk)

    canny = cv2.Canny(gray, th1, th2)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    cv2.imshow("Original", image)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Median Blur", median)
    cv2.imshow("Canny Edge", canny)
    cv2.imshow("Sobel Edge", sobel)
    cv2.imshow("Laplacian Edge", laplacian)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()