import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
mode = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            lm = hand.landmark
            if lm[4].x < lm[3].x:
                mode = 1
            if lm[8].y < lm[6].y:
                mode = 2
            if lm[12].y < lm[10].y:
                mode = 3
            if lm[16].y < lm[14].y:
                mode = 4

    output = frame.copy()

    if mode == 1:
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    if mode == 2:
        kernel = np.array([[0.272,0.534,0.131],[0.349,0.686,0.168],[0.393,0.769,0.189]])
        output = cv2.transform(output, kernel)

    if mode == 3:
        output = cv2.bitwise_not(output)

    if mode == 4:
        output = cv2.GaussianBlur(output,(15,15),0)

    cv2.imshow("Gesture Camera", output)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == 99:
        cv2.imwrite("capture.png", output)

cap.release()
cv2.destroyAllWindows()