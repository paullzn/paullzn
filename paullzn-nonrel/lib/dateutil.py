import time

def date_to_local(date):
	t = time.gmtime()
	try:
		t = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
	except ValueError:
		pass
	temp = time.localtime( time.mktime(t) + 3600 * 8)
	d = str(temp.tm_year) + '-' + str(temp.tm_mon) + '-' + str(temp.tm_mday) + ' ' + str(temp.tm_hour)+":"+str(temp.tm_min)+":"+str(temp.tm_sec)
	return d

