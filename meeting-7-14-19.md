# Helpful tips for Sunday's meeting

Sorry I can't make it, hopefully this document will help some. I don't know how much you know about how the Pi, Linux in general, or Python works, but I'll do my best.

Some of the things here are also on the main README, but for convenience I'll put them here as well.

## Pi Crash Course

### Basic info

To turn on the Pi, have the monitor, keyboard and mouse plugged in before plugging in the power cord.

You won't be asked for a password when the Pi is booting. You may need the password later, so here is the login info.

Username: pi

Password: sandwich

Application shortcuts are on the top left of the screen with more if you click on the raspberry, and settings widgets are on the top right.

You will be using the terminal emulator, which is the icon that looks like `>_`.

### WiFi

I don't know if you'll need WiFi, but here's how to get it.

1. If the Pi is not already on the network, click on the little wifi icon in the top right of the screen and click on attwifi.
2. Open up the Internet browser (globe icon). Go to 1.1.1.1 (IP address, works like a URL for our purposes).
3. Follow the instructions on that webpage.

If you get a complaint about time or date not being correct:

1. Go to raspi-config: Click on the raspberry > Preferences > Raspberry Pi Configuration
2. Go to Localisation
3. Go to Set Timezone...
4. Choose any of the following until you find something that works.
   1. Area = America/Indiana, Location = Indianapolis
   2. Location = GMT
   3. Area = Etc, Location = GMT-4
   
If nothing works, don't worry about it. If all goes well you *shouldn't* need WiFi on the Pi.

### Navigation

Note: If I write something like `[FILE]` as part of a command, replace it with the actual file/directory/whatever you are using. You may need to provide the complete path of the file/directory/whatever.

Directories = folders in a GUI navigator which the Pi *does* have but you probably won't use.

You will start off in the "home" directory `/home/pi`. Everything you need *should* be in here, but I make no promises.

Some useful commands on the terminal:
 * `ls` (or if you're lazy `l` works on this device) will list the contents of the directory you are currently in.
 * `cd [directory one level above/below OR full path to directory]` will change your current directory to wherever you specify.

### Files

To edit files, you've got a few options.

1. Open the text editor GUI: Click on the raspberry > Accessories > Text Editor. The rest should be self-explanatory, just remember to save the file when you're done.
2. Open the code editor GUI: Click on the raspberry > Programming > Geany. Again, the rest should be self-explanatory.
3. Use the text editor in terminal (Vim):
   1. Open up a terminal.
   2. `vim [FILE]` - You may need to add `sudo` to the beginning, depending on the file.
   3. Navigate the file using arrow keys. You can also scroll and use `Page Up` and `Page Down`.
   4. To insert text, type `I`. Once you're done, hit `Esc`.
   5. To close the file, hit `Esc` if you haven't already done so, then type `:x` and press `Enter`.
   6. If you need help, type `:h` and press `Enter`. Alternatively, use Google.
  
To run a Python program, type `python3 [FILE]`. To run a Bash script (you shouldn't need to), type `./[FILE]`.

Speaking of Python...

### Python

I've got all of the programs *written* but I don't know if they're going to work right off the bat. I have already pointed out some things that will need to be changed in the program files.

I know Talal at least knows a programming language (Java I think). Basically, what you need to know:
1. no semicolons
2. no curly braces
3. no "main" function needs to be specified
4. things like `True` and `False` are capitalized
5. `and` instead of `&&`, `or` instead of `||`, `not` instead of `!` - `!` exists but only in the context of `!=`
6. `#` is used for comments. If you need a multi-line comment, use `'''[insert text here]'''` but this is also the way you can specify the purpose of various functions (like Javadoc comments in Java).

I think if you already know one programming language you can pick up what a Python program is trying to do pretty well. Even if you don't, Python is a lot easier to follow for beginners than some other languages (\*cough\* C++).

## TODO

Everything is in the `/home/pi/HALO` directory. When you first open up a terminal window, it will take you to `/home/pi`. So just `cd HALO` and you should be good.

### Sensor Wrangling

**Note:** Whenever you connect/disconnect sensors, turn the Pi off first. Then turn the Pi back on. If you don't do this, it won't harm anything but I don't think the Pi will recognize that a sensor has been plugged in.

To find the address of each I2C sensor (so the accelerometer and the pressure sensor):

1. Open a terminal.
2. `i2cdetect -l` to find the correct bus id
3. `i2cdetect -y [ID]` (ID is probably 1)
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
Tihs means there is a sensor at address 0x1D.

### Temperature Sensor (DS18B20)

The DS18B20 temperature sensor uses a 1-wire interface.

How to set up the Pi: (I hope this works)

1. Connect sensor
2. Open a terminal
3. `sudo modprobe w1–gpio`
4. `sudo modprobe w1-therm`

Find where the sensor is storing data.

1. Open terminal
2. `ls /sys/bus/w1/devices`

Hopefully you will see something that is not `00-180000000000`, `00-580000000000`, `00-980000000000`, or `w1_bus_master1`. Add that to the path in `temp.py`. 

### CO2 Sensor (MHZ-14A)


### GPS Tracker

