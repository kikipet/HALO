# Project HALO

\*Work in progress\*

This is where the programs for the HALO balloon project at Purdue will be stored.

## Dependencies

Some of these packages probably are already installed on the Pi.

### Packages through aptitude
* ~~python-rpi.gpio~~
* ~~python3-smbus~~
* i2c-tools
* libgps23
* gpsd
* gpsd-clients
* libgps-dev
* python-gps

### Other programs/libraries
* direwolf (https://github.com/wb2osz/direwolf)
* RTL-SDR library (https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr)
* Adafruit Blinka (https://pypi.org/project/Adafruit-Blinka/)
  * Also separate libraries for the MMA8451 and MPRLS sensors
* pySerial (https://pyserial.readthedocs.io/en/latest/pyserial.html)

### Other necessary python modules
* time
* picamera

### For potential data processing at the very end
(by no means a definitive list)
* matplotlib
   * GEOS
   * mplot3d
* cartopy

  More dependencies:
   * Cython
   * six
   * PROJ
   * NumPy
   * shapely
   * pyshp
* mpld3

## Other noteworthy things

### General comments

This uses a Raspberry Pi Model 3 B+ running Buster Raspbian.

Go to raspi-config -> Interfaces and enable camera, I2C, serial port, 1-Wire

To find the address of each I2C sensor:

1. `i2cdetect -l` to find the correct bus id
2. `i2cdetect -y [ID]`
This should give an output like this:
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- 1d -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```
There is a sensor at address 0x1D.

### Accelerometer (MMA8451)

An Adafruit sensor, which makes life a lot easier.
Outputs acceleration in X, Y, Z directions in m/s^2.

### Pressure Sensor (MPRLS)

Another Adafruit sensor.
Outputs pressure in hPa, but I added some code that also outputs altitude in feet.

### Temperature Sensor (DS18B20)

The DS18B20 temperature sensor uses a 1-wire interface.

#### How to set up the Pi:

1. Open `/boot/config.txt` as sudo
2. Add `dtoverlay=w1–gpio` to the end of the file
3. Reboot
4. If not already connected, connect sensor
5. `sudo modprobe w1–gpio`
6. `sudo modprobe w1-therm`

### CO2 Sensor (MHZ-14A)

I don't even know what kind of sensor this is. It can use analog (but inaccurate/imprecise), PWM (ok) or serial (the best). We're using serial (UART).
