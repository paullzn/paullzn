import time

def date_to_local(date):
	dat_arr = str(date).split(' ')[0].split('-')
	tim_arr = str(date).split(' ')[1].split(':')
	t = time.mktime(( int(dat_arr[0]), int(dat_arr[1]), int(dat_arr[2]), int(tim_arr[0]), int(tim_arr[1]), float(tim_arr[2]),0,0,0))
	temp = time.localtime( t + 3600 * 8)
	d = str(temp.tm_year) + '-' + str(temp.tm_mon) + '-' + str(temp.tm_mday) + ' ' + str(temp.tm_hour)+":"+str(temp.tm_min)+":"+str(temp.tm_sec)
	return d

