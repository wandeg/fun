import time

def func_timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		ans = func(*args, **kwargs)
		end = time.time()
		print "Time Elapsed for running {} with params [{},{}]= {}".format(func.__name__,args, kwargs, end-start)
		return ans
	return wrapper

