class pid:
    def __init__(self):
        self.kp = 0
        self.ki = 0
        self.kd = 0
        self.ta = 0.1
        self.target = 0
        self.lastError = 0
        self.error = 0
        self.sumError = 0
        self.returnValue = 0
	self.min = -255
	self.max = 255
        print "pid instance created with adr: " + str(self)

    def printData(self):
        print "PID settings\nkp = " + str(self.kp) + "\nki = " + str (self.ki) + "\nkd = " + str(self.kd) 
        print "ta = " + str(self.ta)
        print "target = " + str(self.target)
        print "lastError = " + str(self.lastError)
        print "error = " + str(self.error)
        print "returnValue = " + str(self.returnValue)

    def setKp(self, data):
        self.kp = data

    def setKi(self, data):
        self.ki = data

    def setKd(self, data):
        self.kd = data

    def setTa(self, data):
        self.ta = data

    def setMinMax(self, mi, ma):
	self.min = mi
	self.max = ma

    def setValue(self, data):
        self.error = self.target - data
        self.sumError = self.sumError + self.error

        self.returnValue = self.kp * self.error + self.ki * self.ta * self.sumError + self.kd * (self.error - self.lastError) / self.ta
        self.lastError = self.error

    def setTarget(self, data):
        self.target = data;

    def getValue(self):
	if self.returnValue > self.max:
	   self.returnValue = self.max
	if self.returnValue < self.min:
	   self.returnValue = self.min
        return self.returnValue


