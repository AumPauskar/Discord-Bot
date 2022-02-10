import time
def SendTime():
	curtime = str(time.strftime('%H : %M : %S'))
	return curtime
def SendDate():
	curdate = str(time.strftime('%Y / %m / %d'))
	return curdate