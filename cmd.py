#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

PIN_USB = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_USB,GPIO.OUT)

if sys.argv[1] == "usbon":
    GPIO.output(PIN_USB,GPIO.HIGH)
elif sys.argv[1] == "usboff":
    GPIO.output(PIN_USB,GPIO.LOW)

#GPIO.cleanup()
