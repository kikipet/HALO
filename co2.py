import time, serial

mhz = serial.Serial("/dev/ttyAMA0", 9600, timeout=1) # replace "/dev/ttyAMA0" with actual location of sensor
packet = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
zero =  [0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2]

mhz.write(bytearray(packet))
res = mhz.read(size=9)
res = bytearray(res)

while True:
    co2 = (res[2]<<8)|res[3]
    print(co2)
    time.sleep(10)
