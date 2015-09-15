#!/usr/bin/python

import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
pin = 17

class motor:
	def __init__(self, pwmpin, dirpin): # pwm pin, then dir pin
	  self.pwmPin = pwmpin
	  self.dirPin = dirpin
          GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
	  GPIO.setup(self.pwmPin, GPIO.OUT)             
	  GPIO.setup(self.dirPin, GPIO.OUT)           
          self.pwm = GPIO.PWM(self.pwmPin, 100)
          self.pwm.start(0)
	  print "motor ready pwm pin " + str (self.pwmPin) + " dirpin " + str(self.dirPin)

	def setPwm(self, pwmValue):
	  #print "set pwmValue to " + str(pwmValue)
	  self.pwm.ChangeDutyCycle(pwmValue)

	def forward(self):
	  GPIO.output(self.dirPin, 1)

	def reverse(self):
	  GPIO.output(self.dirPin, 0)
	

	def __del__(self):
 	  self.setPwm(0)
	  GPIO.cleanup(self.pwmPin)
	  GPIO.cleanup(self.dirPin)
	  print "motor destroyed"
	
