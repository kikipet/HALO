The DS18B20 temperature sensor uses a 1-wire interface.

**How to set up the Pi:**

1. Open `/boot/config.txt` as sudo
2. Add `dtoverlay=w1–gpio` to the end of the file
3. Reboot
4. If not already connected, connect sensor
5. `sudo modprobe w1–gpio`
6. `sudo modprobe w1-therm`
