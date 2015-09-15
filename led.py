#!/usr/bin/python

import RPi.GPIO as GPIO            # import RPi.GPIO module  

class led:
	def __init__(self, pin): # pin
	  self.pin = pin
          GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
	  GPIO.setup(self.pin, GPIO.OUT)             

	def on(self):
	  GPIO.output(self.pin, 1)

	def off(self):
	  GPIO.output(self.pin, 0)

	def toggle(self):
	  GPIO.output(self.pin, not GPIO.input(self.pin))

	def __del__(self):
	  GPIO.cleanup(self.pin)
	
