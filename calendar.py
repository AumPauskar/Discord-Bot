import time
def SendTime():
	curtime = time.strftime('%H') + ':' +time.strftime('%M') + ':' + time.strftime('%S')
	return curtime
def SendDate():
	curdate = time.strftime('%d') + '/' + time.strftime('%m') + '/' + time.strftime('%y')
	return curdate