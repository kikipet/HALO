import time, math, smbus

def read_temp():
	'''read_temp() -> float
	Reads data from thermometer
	Returns temperature (Celsius)'''
	pass

def read_barometer():
	'''read_barometer() -> tuple
	Reads data from barometer
	Returns pressure (hPa), altitude (feet)'''
	# maybe return in more "standard" unit of pressure
	pass

def read_accelerometer():
	'''read_accelerometer() -> tuple
	Reads data from accelerometer
	Returns'''
	pass

def read_air():
	'''TBD'''
	pass

# 1 big log file
log = open("sensor-data-log", "w")

# several log files
tempFile = open("temperature", "w")
baroFile = open("barometer", "w") # pressure and altitude
accelFile = open("accelerometer", "w")
airFile = open("air-quality", "w") # ???

while True:
	# bad condition for while loop - it should stop at *some* point
	temp = read_temp()
	baro = read_baro()
	accel = read_accel()
	log.write("{} {} {} {} [...]".format(time.strftime("%H%M%S", time.localtime()), temp + "\u00b0 C", baro[0], baro[1], [...]))
