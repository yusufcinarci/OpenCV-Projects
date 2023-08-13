# **** LIBRARY SETUPS ****
# pip install mediapipe
# pip install opencv-python

import mediapipe as mp
import cv2
import numpy as np
import pyrebase
import time

# içerikler - contants
ml = 150
max_x, max_y = 300 + ml, 50
curr_tool = "Arac Sec"
time_init = True
rad = 40
var_inits = False
thick = 2
prevx, prevy = 0, 0

firebaseConfig = {
  "apiKey": "AIzaSyB_S2tR_2YsRrM-KQUHsS_Uj_q1kmGBetM",
  "authDomain": "armrobot-98491.firebaseapp.com",
  "databaseURL": "https://armrobot-98491-default-rtdb.firebaseio.com/",
  "projectId": "armrobot-98491",
  "storageBucket": "armrobot-98491.appspot.com",
  "messagingSenderId": "755214414021",
  "appId": "1:755214414021:web:8807c50e5d8b4c22bec0ac",
  "measurementId": "G-YMMDCZZQ68"
};

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
size = 4

# Araçları seçme fonksiyonu - get tools function
def getTool(x):
    if x < 65 + ml:
        return "Agiz_ac"

    elif x < 115 + ml:
        return "Agiz_kapat"

    elif x < 165 + ml:
        return "Sol"

    elif x < 215 + ml:
        return "Sag"

    elif x<265+ml:
        return "Yukari"
    else:
        return "Asagi"


def index_raised(yi, y9):
    if (y9 - yi) > 40:
        return True

    return False


hands = mp.solutions.hands
hand_landmark = hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.6, max_num_hands=1)
draw = mp.solutions.drawing_utils

# çizim araçları - drawing tools
tools = cv2.imread("1.png")
tools = tools.astype('uint8')

mask = np.ones((480, 640)) * 255
mask = mask.astype('uint8')

cap = cv2.VideoCapture(0)

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
    op = hand_landmark.process(rgb)
    users = db.child("users2").child("position").shallow().get()

    #print(users.val())

    if op.multi_hand_landmarks:

        for i in op.multi_hand_landmarks:
            draw.draw_landmarks(frm, i, hands.HAND_CONNECTIONS)
            x, y = int(i.landmark[8].x * 640), int(i.landmark[8].y * 480)

            if x < max_x and y < max_y and x > ml:
                if time_init:
                    ctime = time.time()
                    time_init = False
                ptime = time.time()

                cv2.circle(frm, (x, y), rad, (0, 255, 255), 1)
                rad -= 1

                if (ptime - ctime) > 0.8:
                    curr_tool = getTool(x)
                    print("Secilen arac : ", curr_tool)
                    time_init = True
                    rad = 40

                    if curr_tool == "Agiz_ac":
                        print("Agiz acildi")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Agiz_ac'
                        })

                    elif curr_tool == "Agiz_kapat":
                        print("Agiz kapatildi")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Agiz_kapat'
                        })

                    elif curr_tool == "Sol":
                        print("Sola Dönecek")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Sol'
                        })
                    elif curr_tool == "Sag":
                        print("Saga Dönecek")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Sag'
                        })
                    elif curr_tool == "Yukari":
                        print("Yukari Dönecek")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Yukari'
                        })
                    elif curr_tool == "Asagi":
                        print("Asagi Dönecek")
                        hopper_ref = db.child("users2")
                        hopper_ref.update({
                            'position': 'Asagi'
                        })



    op = cv2.bitwise_and(frm, frm, mask=mask)
    frm[:, :, 1] = op[:, :, 1]
    frm[:, :, 2] = op[:, :, 2]

    frm[:max_y, ml:max_x] = cv2.addWeighted(tools, 0.7, frm[:max_y, ml:max_x], 0.3, 0)

    cv2.putText(frm, curr_tool, (320 + ml, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Cizim Uygulamasi", frm)

    if cv2.waitKey(1)  & 0xFF==ord('q'):# EXIT >>> ESC Key

        break
cv2.destroyAllWindows()
cap.release()