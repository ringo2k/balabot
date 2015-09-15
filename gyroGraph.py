#!/usr/bin/python
from mpu6050 import mpu6050
#from pylab import *
import time
import matplotlib.pyplot as plt

# gyro settings
gyro=mpu6050()

gyro.setFilter(0)

plt.ion()
data = []
dataGyro = []
value = gyro.getAccelX()
filteredData = [value]
value = gyro.getGyroY()
filteredDataGyro = [value]

angle = value
angleData = []


for i in range(18000000):
	value = gyro.getAccelX() * 90.0
	accel = value
	data.append(value)
	filteredData.append(0.9 * filteredData[-1] + 0.1 * value) 
	value = gyro.getGyroY() * -1.0
	dataGyro.append(value)
	filteredDataGyro.append(0.9 * filteredDataGyro[-1] + 0.1 * value) 
	angle = (0.9) * (angle + value * 0.01) + (0.1 * filteredData[-1])
	angleData.append(angle)
	if not i % 80:
		plt.delaxes()
		#plt.plot(data, color="black")
		plt.plot(filteredData, color="red")
		#plt.plot(dataGyro, color="black")
		#plt.plot(filteredDataGyro, color="cyan")
		#plt.plot(angleData, color="green")
		plt.draw()
		print str(angle)
	else:
		time.sleep(0.01)

if plt.waitforbuttonpress(0.01) != None:
	quit()
