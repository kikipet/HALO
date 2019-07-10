import time, math, smbus, RPi.GPIO as GPIO, board, busio, adafruit_mprls, adafruit_mma8451, serial, picamera

cam = picamera.PiCamera()

path = "/sys/bus/w1/devices" # ?
tempData = open(path+"w1_slave", "r") # add path to the file name

i2c = busio.I2C(board.SCL, board.SDA)
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
mma = adafruit_mma8451.MMA8451(i2c)
mhz = serial.Serial("/dev/ttyAMA0",9600,timeout=1) # replace "/dev/ttyAMA0" with actual location of sensor
packet = [0xff,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79] # is this what I want or do I need to change values?
zero = [0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2]
	
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
	x, y, z = mma.acceleration
	return (x, y, z)

def read_co2():
	'''read_co2() -> float (int?)
	Reads data from CO2 sensor
	Returns concentration of CO2 (ppm)'''
	mhz.write(bytearray(packet))
	res = mhz.read(size=9)
	res = bytearray(res)
	return (res[2]<<8)|res[3]
	# not sure if any of this is right

# 1 big log file
log = open("sensor-data-log", "w")

c = 0

# non-GPS data should be collected every 10 seconds or so

while True:
	# bad condition for while loop - it should stop at *some* point
	temp = read_temp()
	baro = read_baro()
	accel = read_accel()
	co2 = read_co2()
	log.write("{}    {:6.3f} \u00b0C    {:4.3f} hPa  {:6.3f} ft    X: {:.3f} m/s\u00b2  Y: {:.3f} m/s\u00b2  Z: {:.3f} m/s\u00b2    {} ppm".format\
		  (time.strftime("%H:%M:%S", time.gmtime(time.time()-14400))), temp, baro[0], baro[1], accel[0], accel[1], accel[2], co2))
	if baro[1] < 30000 or (baro[1] >= 30000 and c == 0):
		# hm change capture rate based on altitude? (like at a certain point the view each minute will not change all too much)
		# a bit arbitrary
		cam.capture("IMG_" + time.strftime("%H%M%S", time.gmtime(time.time()-14400))) + ".jpg") # localtime or gmtime?
	time.sleep(120)
	c = 1 - c
