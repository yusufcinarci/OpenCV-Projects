#Kütüphaneler
from time import sleep
import datetime
import RPi.GPIO as GPIO
import pyrebase
import cv2
import Adafruit_DHT
import tkinter as tk
from tkinter import messagebox
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


pwm = GPIO.PWM(11,50)
pwm.start(0)

pwm2 = GPIO.PWM(13,50)
pwm2.start(0)

pwm3=GPIO.PWM(40,50)
pwm3.start(0)

pwm4 = GPIO.PWM(15,50)
pwm4.start(0)
sleep(2)


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

while 1:
    users = db.child("users2").child("position").shallow().get()
    print(users.val())
    position = str(users.val())
    while 1:
        if(position =="Agiz_ac"):
            pwm.ChangeDutyCycle(11)
            sleep(2)
            pwm.ChangeDutyCycle(0)
            break
        elif(position =="Agiz_kapat"):
            pwm.ChangeDutyCycle(8)
            sleep(2)
            pwm.ChangeDutyCycle(0)
            break
        elif(position =="Sol"):
            pwm2.ChangeDutyCycle(4)
            sleep(2)
            pwm2.ChangeDutyCycle(0)
            break
        elif(position =="Sag"):
            pwm2.ChangeDutyCycle(6)
            sleep(2)
            pwm2.ChangeDutyCycle(0)
            break
        elif(position=="Yukari"):
            pwm3.ChangeDutyCycle(7)
            sleep(2)
            pwm3.ChangeDutyCycle(0)
            break
        elif(position=="Asagi"):
            pwm4.ChangeDutyCycle(4.5)
            sleep(2)
            pwm4.ChangeDutyCycle(0)
            break
        
        else:
            pass
            break
    


