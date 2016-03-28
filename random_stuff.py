from utils import func_timer

def max_odd(x,y,z):
	"""Takes 3 integers and returns the largest odd number among them"""
	highest = x
	if y>highest and y %2 != 0:
		highest = y
	if z>highest and z%2 != 0:
		highest = z
	if highest %2 != 0:
		return highest
	return "Yo!!! please get serious and gimme odd numbers"

