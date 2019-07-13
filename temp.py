import time

path = "/sys/bus/w1/devices/" # finish the path
tempData = open(path+"w1_slave", "r") # correct file name if necessary

def read_temp():
    lines = tempData.readLines()
    while lines[0].strip()[-3:] != "YES":
        lines = tempData.readLines()
    return float(lines[1][lines[1].find("t=")+2:])/1000

while True:
    print(read_temp())
    time.sleep(10)
