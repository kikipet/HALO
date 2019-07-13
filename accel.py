import busio, adafruit_mma8451, time

i2c = busio.I2C(board.SCL, board.SDA);
mma = adafruit_mma8451.MMA8451(i2c, address=0x1D)

x, y, z = mma.acceleration

while True:
    print((x, y, z))
    time.sleep(10)
