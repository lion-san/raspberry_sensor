import RPi.GPIO as GPIO
import requests
import datetime

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
      print "MOTION"
      time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
      requests.post("http://maker.ifttt.com/trigger/human_detect/with/key/cSdQ_oKHTolntlARUFAKD8", json={"value1": "Event from Raspberry Pi", "value2":time})

    else:
      GPIO.output(led, GPIO.LOW)

    sleep(1)


except KeyboardInterrupt:
  print "hogehogehogheogheohgoee"
  GPIO.cleanup()
  pass
