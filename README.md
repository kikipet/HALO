# Project HALO

\*Work in progress\*

This is where the programs for the HALO balloon project at Purdue will be stored.

## Dependencies

Some of these packages probably are already installed on the Pi.

**Packages through aptitude**
* python-rpi.gpio
* python3-smbus
* i2c-tools
* libgps23
* gpsd
* gpsd-clients
* libgps-dev
* python-gps

**Other programs/libraries**
* direwolf (https://github.com/wb2osz/direwolf)
* RTL-SDR library (https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr)
* Adafruit Blinka (https://pypi.org/project/Adafruit-Blinka/)

**Other necessary python modules**
* time
* picamera

**For potential data processing at the very end**
(by no means a definitive list)
* matplotlib
   * basemap
   * GEOS
   * mplot3d
* mpld3

## Other noteworthy things

The DS18B20 temperature sensor uses a 1-wire interface.

**How to set up the Pi:**

1. Open `/boot/config.txt` as sudo
2. Add `dtoverlay=w1–gpio` to the end of the file
3. Reboot
4. If not already connected, connect sensor
5. `sudo modprobe w1–gpio`
6. `sudo modprobe w1-therm`
