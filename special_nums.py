import random
import math

def triangular(n):
	"""Returns the nth triangular digit (sum of all consecutive digits from 1 up to n)"""
	return (n*(n+1))/2

def triangular_diff(m,n):
	"""Returns the difference between two triangular numbers m and n"""
	return triangular(n) - triangular(m-1)

def triangular_two_digits(m,n):
	"""Returns the sum of all consecutive digits between two numbers m and n"""
	return triangular_diff(m,n)

def consecutive_triangulars(n):
	"""Gets conseutive triangulars of a random n and checks if their sum is an square
	t(n)+ t(n-1) = n**2"""
	middle = triangular(n)
	first = triangular(n-1)
	last = triangular(n+1)

	return math.sqrt(first+middle).is_integer() and math.sqrt(middle+last).is_integer()

def reverse_triangular(n):
	"""Finds two triangular numbers whose sum is n"""
	root = math.sqrt(n)
	assert root.is_integer() == True, "Invalid number"
	return int(triangular(root)), int(triangular(root-1))


assert triangular(3) == (1+2+3)
assert triangular_two_digits(6,11) == (6+7+8+9+10+11)
assert triangular_diff(200,200) == 200

val = random.randint(0,10000000)
assert consecutive_triangulars(val) == True
assert reverse_triangular(25) == (15,10)
