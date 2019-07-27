import time, serial

mhz = serial.Serial("/dev/serial0", 9600)
#mhz = serial.Serial("/dev/ttyS0", 9600, timeout=1)
packet = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]

while True:
    mhz.write(bytearray(packet))
    time.sleep(2)
    res = mhz.read(size=9)
    time.sleep(2)
    res = bytearray(res)
    co2 = (res[2]<<8)|res[3]
    print(co2)
    time.sleep(10)
