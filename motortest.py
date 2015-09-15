#!/usr/bin/python

import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
pin = 17
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(pin, GPIO.OUT)           # set GPIO24 as an output   

pwm = GPIO.PWM(pin, 100)

freq = 0;
pwm.start(0)
  
try:  
    while True:  
	print "status pin %d to %d" % (pin,freq,)
	freq = freq + 1
	if freq > 100:
	  freq = 0
	pwm.ChangeDutyCycle(freq)
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    pwm.stop()
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
