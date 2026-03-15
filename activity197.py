import cv2
import numpy as np

cap = cv2.VideoCapture(0)
mode = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if mode == 1:
        b,g,r = cv2.split(frame)
        frame = cv2.merge([b*0, g*0, r])
    elif mode == 2:
        b,g,r = cv2.split(frame)
        frame = cv2.merge([b*0, g, r*0])
    elif mode == 3:
        b,g,r = cv2.split(frame)
        frame = cv2.merge([b, g*0, r*0])
    elif mode == 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.Canny(gray,100,200)
    elif mode == 5:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.Laplacian(gray,cv2.CV_64F)
        frame = np.uint8(np.absolute(frame))

    cv2.imshow("Image Processing", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n'):
        mode = 0
    elif key == ord('r'):
        mode = 1
    elif key == ord('g'):
        mode = 2
    elif key == ord('b'):
        mode = 3
    elif key == ord('c'):
        mode = 4
    elif key == ord('l'):
        mode = 5

cap.release()
cv2.destroyAllWindows()