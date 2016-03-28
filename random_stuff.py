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

def max_odd_input(n):
	"""Takes n positive integers from the user's input and returns the largest odd number among them"""
	count = 0
	highest = 0
	while count < n:
		num = int(raw_input("Please insert digit: "))
		if num>highest and num %2 != 0:
			highest = num
		count +=1
	if highest %2 != 0:
		return highest
	return "Yo!!! please get serious and gimme odd numbers"
