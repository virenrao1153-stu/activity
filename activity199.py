import cv2
import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append((cx,cy))

            if lmList:
                x1,y1 = lmList[4]
                x2,y2 = lmList[8]
                cx,cy = (x1+x2)//2,(y1+y2)//2

                cv2.circle(img,(x1,y1),10,(255,0,0),cv2.FILLED)
                cv2.circle(img,(x2,y2),10,(255,0,0),cv2.FILLED)
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
                cv2.circle(img,(cx,cy),10,(0,0,255),cv2.FILLED)

                length = math.hypot(x2-x1,y2-y1)

                vol = np.interp(length,[30,200],[minVol,maxVol])
                volume.SetMasterVolumeLevel(vol,None)

                bright = np.interp(length,[30,200],[0,100])
                sbc.set_brightness(int(bright))

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()