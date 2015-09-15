#!/usr/bin/python 

from motor import motor
from led import led
from time import sleep             # lets us have a delay  
from pid import pid
from mpu6050 import mpu6050
import RPi.GPIO as GPIO            # import RPi.GPIO module  


# set up inputs 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # blue button
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # yellow button




motorA = motor(17,27)
motorB = motor(22,10)

gyro=mpu6050()
gyro.setFilter(2)

greenLed = led(24)
yellowLed = led(25)

greenLed.on()
yellowLed.off()

# regulator settings
Ta = 0.05
Time =120 / Ta
regulator = pid()
regulator.setKp(20)
#regulator.setKi(0.2)
#regulator.setKd(3)
regulator.setTa(4*Ta)
regulator.setMinMax(-100,100)
regulator.setTarget(-1.2)
pwmActive = False

angle = 0
plotDataiFile = open("plot.dat", "w")

def blueButtonPressed(channel):
  print "blue Button pressed"
  sleep(0.5)
  while GPIO.input(18) != GPIO.LOW:
    sleep(0.5)
  global pwmActive
  pwmActive = not pwmActive

def yellowButtonPressed(channel):
  print "yellow Button pressed"
  sleep(0.3)
  while GPIO.input(23) != GPIO.LOW:
    sleep(0.3)

def complementaerFilter(acc, gyro, angle):
  coeff = 0.95
  angle = (coeff) * (float(angle) + float(Ta) * float(gyro)) + ((1.0-coeff) * acc)
  return angle

GPIO.add_event_detect(18, GPIO.FALLING, callback=blueButtonPressed)
GPIO.add_event_detect(23, GPIO.FALLING, callback=yellowButtonPressed)
try:  
    #first we let all get stable
    print "wait till values are stable"
    greenLed.off()
    yellowLed.on()
    sleep(1)
    diff = 10
    while diff > 1:
      diff = angle
      for i in range(0,10):
	sleep(0.1)
        value = (gyro.getAccelX())
        accel = value * 90.0
        accel = accel - 5.0 # offset
        value = (gyro.getGyroY() * -1.0)
        angle =  complementaerFilter(accel, value,angle)
      diff = abs(diff - angle)
    print "finish"
         
    for i in range(0,int(Time)):
        value = (gyro.getAccelX())
        accel = value * 90.0
        accel = accel - 5.0 # offset
        value = (gyro.getGyroY() * -1.0)
        angle =  complementaerFilter(accel, value,angle)
	print angle
	regulator.setValue(angle)
        if pwmActive:
	  pwm = regulator.getValue()
	  greenLed.on()
	else:
	  pwm = 0
	  greenLed.off()
	plotDataiFile.write(str(angle) + "\t" + str(pwm) + "\n")	
	if pwm < 0:
	  pwm = pwm * -1
	  motorA.reverse()
	  motorA.setPwm(pwm)
	  motorB.reverse()
	  motorB.setPwm(pwm)
	else:
	  motorA.forward()
	  motorA.setPwm(pwm)
	  motorB.forward()
	  motorB.setPwm(pwm)
	   
	yellowLed.toggle()
        sleep(Ta)                 
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	print "finish"
