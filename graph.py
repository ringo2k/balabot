#!/usr/bin/python
from mpu6050 import mpu6050
import matplotlib.pyplot as plt
import time

print "making a graf"

gyro=mpu6050()

print "x accel:" + str(gyro.getAccelX())

data = []

plt.show(block=False)
for i in range(10):
	data.append(gyro.getAccelX())
	time.sleep(1)
	plt.plot(data)
