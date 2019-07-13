import time, math, smbus, RPi.GPIO as GPIO, board, busio, adafruit_mprls, adafruit_mma8451, serial, picamera


# path = "/sys/bus/w1/devices" # ?
# tempData = open(path+"w1_slave", "r") # add path to the file name

i2c = busio.I2C(board.SCL, board.SDA)
# mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
mma = adafruit_mma8451.MMA8451(i2c, address=0x1D)
#mhz = serial.Serial("/dev/ttyAMA0",9600,timeout=1) # replace "/dev/ttyAMA0" with actual location of sensor
# packet = [0xff,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79] # is this what I want or do I need to change values?
# zero = [0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2]
	
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

# temp = read_temp()
# baro = read_baro()
while True:
    accel = read_accel()
    print(accel)
    time.sleep(10)
# co2 = read_co2()
