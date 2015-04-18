import RPi.GPIO as GPIO
from flask import Flask
import time

PIN_USB = 12
PIN_WEB = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_USB,GPIO.OUT)
GPIO.setup(PIN_WEB,GPIO.OUT)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/usbon")
def usbOn():
    GPIO.output(PIN_USB,GPIO.HIGH)
    return "GPIO.HIGH and USB.ON"

@app.route("/usboff")
def usbOff():
    GPIO.output(PIN_USB,GPIO.LOW)
    return "GPIO.LOW and USB.OFF"

@app.route("/test")
def test():
    count = 0
    while count < 5:
        count += 1
        GPIO.output(PIN_USB,GPIO.LOW)
        time.sleep(5)
        GPIO.output(PIN_USB,GPIO.HIGH)
        time.sleep(5)

if __name__ == "__main__":
    GPIO.output(PIN_WEB,GPIO.HIGH)
    app.run(host='0.0.0.0',port=80)
    GPIO.cleanup()
