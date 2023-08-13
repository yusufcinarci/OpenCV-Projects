-----------------------------------------------

# Arm control with OpenCv,Mediapipe and Firebase
It is the robot arm control project of our Computer Vision works with Opencv. In this project, a Firebase-based robot project was realized by using Opencv and Mediapipe artificial intelligence libraries. Below I tried to explain the details of the project step by step.

## Arm control with OpenCv,Mediapipe and Firebase

First, we will download the libraries we will use.
```Python
import mediapipe as mp
import cv2
import numpy as np
import pyrebase
import time
```

### The code block we linked to Firebase

```Python
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
```
After registering Firebase from Google, create your project file and paste the drawn part in our code.


![image](https://user-images.githubusercontent.com/67556543/181937768-3ef4a23d-9acd-47ff-b420-a3b14e03f6e4.png)

**NOTE**

The code block I have shown below will not be in firebase. Don't forget to add it. Don't forget to add it to the code block by typing its own link in your Firebase account where I have shown in the picture.

```Python
"databaseURL": "https://armrobot-98491-default-rtdb.firebaseio.com/",
```
![image](https://user-images.githubusercontent.com/67556543/181940174-38953af5-1e58-4b52-a56e-709a9d181a18.png)

**NOTE2**

Also, do not forget to name users2 and string as a variable for the firebase base you will create.

![image](https://user-images.githubusercontent.com/67556543/181944242-afa1982a-3d3d-4322-b5e0-b7d1be42f05a.png)

**NOTE3**

Do not forget to apply the changes you will make on the Firebase base in the raspberrypi_code part.

Raspberrypi_code.py file should be run inside Raspberry Pi development board. The other main.py should be run on computer.

Raspberry pi connection pins of robotic arm

```Python
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
```

![image](https://user-images.githubusercontent.com/67556543/181952328-b0049466-522f-4a12-9df0-f40bb0a595e7.png)

Wiring of the servo motors of the robotic arm on the breadboard

![image](https://user-images.githubusercontent.com/67556543/181953686-9304b1fe-4a4f-4db1-aadc-6a54004b273b.png)
