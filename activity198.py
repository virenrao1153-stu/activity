import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,120,70])
    upper = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5,5),np.uint8)

    mask = cv2.dilate(mask,kernel,iterations=2)
    mask = cv2.GaussianBlur(mask,(5,5),0)

    contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 3000:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cx = x + w//2
            cy = y + h//2
            cv2.circle(frame,(cx,cy),5,(255,0,0),-1)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()