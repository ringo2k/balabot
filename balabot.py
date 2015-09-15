#!/usr/bin/python 

from motor import motor
from led import led
from time import sleep             # lets us have a delay  
from pid import pid
from mpu6050 import mpu6050

motorA = motor(17,27)
motorB = motor(22,10)

gyro=mpu6050()
gyro.setFilter(2)

greenLed = led(24)
yellowLed = led(25)
angle = 0

greenLed.on()
yellowLed.off()

# regulator settings
Ta = 0.05
Time =20 / Ta
regulator = pid()
regulator.setKp(18)
#regulator.setKi(0.2)
#regulator.setKd(3)
regulator.setTa(4*Ta)
regulator.setMinMax(-100,100)
#regulator.setTarget(-3.2)

plotDataiFile = open("plot.dat", "w")

try:  
    #while True:  
    for i in range(0,int(Time)):
	value = (gyro.getAccelX())
	accel = value * 90.0
	accel = accel - 5.0 # offset
	value = (gyro.getGyroY() * -1.0)
	coeff = 0.95
	angle = (coeff) * (angle + Ta* value) + ((1.0-coeff) * accel)
	print angle
	regulator.setValue(angle)
	pwm = 0#regulator.getValue()
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
	   
	greenLed.toggle()
	yellowLed.toggle()
        sleep(Ta)                 
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	print "finish"
