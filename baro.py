import time, math, busio, adafruit_mprls

i2c = busio.I2C(board.SCL, board.SDA)
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)
p = mpr.pressure
alt = (10**(math.log10(p/1013.25) + 6) - 1) / 6.8755856 * -1 # can be fixed easily (in meters)

while True:
    print ((p, alt))
    time.sleep(10)
