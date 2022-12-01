import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN) 

while True:
    state = GPIO.input(pin)
    if state:
        print(1)
    else:
        print(0)
    time.sleep(0.01)


