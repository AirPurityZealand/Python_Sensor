import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setmode(GPIO.BCM)  
GPIO.setup(pin, GPIO.IN) 


def measure_co2():
    state = GPIO.input(pin)
    if state:
        return 1
    else:
        return 0
    time.sleep(0.01)