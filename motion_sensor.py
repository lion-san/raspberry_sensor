import RPi.GPIO as GPIO
from time import sleep

sensor = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

try:
        while True:        
                print GPIO.input(sensor)
                sleep(1)

except KeyboardInterrupt:
        pass

GPIO.cleanup()
