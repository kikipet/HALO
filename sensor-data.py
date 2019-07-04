import time, math, smbus, RPi.GPIO as GPIO, board, busio, adafruit_mprls, adafruit_mma8451

tempData = open("w1_slave", "r") # add path to the file name

# i2c = busio.I2C(board.SCL, board.SDA)
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
	
def read_temp():
	'''read_temp() -> float
	Reads data from thermometer
	Returns temperature (Celsius)'''
	lines = tempData.readLines()
	while lines[0].strip()[-3:] != "YES":
		lines = tempData.readLines()
	return float(lines[1][lines[1].find("t=")+2:])/1000

def read_baro():
	'''read_barometer() -> tuple
	Reads data from barometer
	Returns pressure (hPa), altitude (feet)'''
	# maybe return in more "standard" unit of pressure
	p = mpr.pressure # this is float right?
	return (p, (10**(math.log10(p/1013.25) + 6) - 1) / 6.8755856 * -1)

def read_accel():
	'''read_accel() -> tuple
	Reads data from accelerometer
	Returns acceleration in x, y, z directions'''
	pass

def read_air():
	'''TBD'''
	pass

# 1 big log file
log = open("sensor-data-log", "w")

while True:
	# bad condition for while loop - it should stop at *some* point
	temp = read_temp()
	baro = read_baro()
	accel = read_accel()
	log.write("{} {} {} {} [...]".format(time.strftime("%H%M%S", time.localtime()), temp + "\u00b0 C", baro[0], baro[1], [...]))
	time.sleep(120)
