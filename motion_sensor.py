import RPi.GPIO as GPIO
from time import sleep

sensor = 21
led = 2

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
  while True:        
    val = GPIO.input(sensor)
    print GPIO.input(sensor)

    if val == 1:
      GPIO.output(led, GPIO.HIGH)

    else:
      GPIO.output(led, GPIO.LOW)

    sleep(1)

except KeyboardInterrupt:
        pass

GPIO.cleanup()
