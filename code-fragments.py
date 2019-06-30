import time

# time.ctime() gives something like "Sat Jun 29 02:27:50 2019"

# what will be sent to the log
# "{} {} {} [...]".format(time.ctime(), temp, alt, [...])... well the result of this

# do the sensors write up data into separate files? if so then i'll have to read in a bunch of files :|

# honestly a lot of this is going to depend on exactly what hardware we're using

# account for possibly not receiving data from a sensor - just repeat the last entry or say N/A or something like that?

while True:
	# code?
	# better condition for while loop?
	# read data from their respective sensors
	# write data to some file
	time.sleep(30) # not actually sure how often I should collect data
