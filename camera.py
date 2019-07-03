import picamera

cam = picamera.PiCamera()
while True:
	time.sleep(60)
	cam.capture("IMG_" + time.strftime("%H%M%S", time.localtime()) + ".jpg") # localtime or gmtime?
	# hm change capture rate based on altitude? (like at a certain point the view each minute will not change all too much)
