#!/usr/bin/python

import smbus

class mpu6050:
	def __init__(self):
		print "new mpu6050 instance created: " + str(self)
		self.bus = smbus.SMBus(1)
		self.i2cadress = 0x68
		# power up the gyro
		self.bus.write_byte_data(self.i2cadress,0x6b, 0) 

	def readWord(self, adress):
		hval= self.bus.read_byte_data(self.i2cadress,adress)
		lval= self.bus.read_byte_data(self.i2cadress,adress + 1)
		val = (hval << 8) + lval
		if (val >= 0x8000):
			return -((65535 - val) + 1)
		else:
			return val

	def setSampleRate(self, rate):
		self.bus.write_byte_data(self.i2cadress,0x19, rate)

	def setFilter(self, hz):
		self.bus.write_byte_data(self.i2cadress,0x1A, hz)

	def readTemperature(self):
		return ((int(self.readWord(0x41) & 0xffff) / 340.0) + 36.53)

	def getAccelX(self):
		return (self.readWord(0x3b)/ 16384.0) 
	def getAccelY(self):
		return (self.readWord(0x3d)/ 16384.0)
	def getAccelZ(self):
		return (self.readWord(0x3f)/ 16384.0)

	def getGyroX(self):
		return (self.readWord(0x43)/ 131.0) 
	def getGyroY(self):
		return (self.readWord(0x45)/ 131.0)
	def getGyroZ(self):
		return (self.readWord(0x47)/ 131.0)
		

#print "gyro data"

#gyro=mpu6050()

#gyro.setFilter(6)

#print "temperature: " + str(gyro.readTemperature())

#print "x accel:" + str(gyro.getAccelX())
#print "y accel:" + str(gyro.getAccelY())
#print "z accel:" + str(gyro.getAccelZ())

