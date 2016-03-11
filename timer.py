import time

def func_timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		ans = func(*args, **kwargs)
		end = time.time()
		print "Time Elapsed for running {} = {}".format(func.__name__,end-start)
		return ans
	return wrapper

