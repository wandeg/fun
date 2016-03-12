import random
import math
from utils import func_timer

@func_timer
def triangular(n):
	"""Returns the nth triangular digit (sum of all consecutive digits from 1 up to n)"""
	return (n*(n+1))/2

@func_timer
def triangular_diff(m,n):
	"""Returns the difference between two triangular numbers m and n"""
	return triangular(n) - triangular(m-1)

@func_timer
def triangular_two_digits(m,n):
	"""Returns the sum of all consecutive digits between two numbers m and n"""
	return triangular_diff(m,n)

@func_timer
def consecutive_triangulars(n):
	"""Gets conseutive triangulars of a random n and checks if their sum is an square
	t(n)+ t(n-1) = n**2"""
	middle = triangular(n)
	first = triangular(n-1)
	last = triangular(n+1)

	return math.sqrt(first+middle).is_integer() and math.sqrt(middle+last).is_integer()

@func_timer
def reverse_triangular(n):
	"""Finds two triangular numbers whose sum is n"""
	root = math.sqrt(n)
	assert root.is_integer() == True, "Invalid number"
	return int(triangular(root)), int(triangular(root-1))

@func_timer
def get_factors(n):
	"""Gets all the factors of an integer"""
	facts = set()
	top = n//2
	for i in range(1,top):
		val = n%i
		if val == 0:
			quot = n/i
			if quot != n:
				facts.add(quot)
			facts.add(i)

	return sorted(list(facts))

@func_timer
def check_abundance(n):
	"""Check whether number is perfect, abundant or deficient"""
	sum_fact = sum(get_factors(n))
	if sum_fact > n:
		return 1
	elif sum_fact < n:
		return -1
	return 0


def tests():
	"""Test code is correct"""
	assert triangular(3) == (1+2+3)
	assert triangular_two_digits(6,11) == (6+7+8+9+10+11)
	assert triangular_diff(200,200) == 200

	val = random.randint(0,10000000)
	assert consecutive_triangulars(val) == True
	assert reverse_triangular(25) == (15,10)
	assert check_abundance(8) == -1
	assert check_abundance(28) == 0
	assert check_abundance(18) == 1

if __name__ == '__main__':
	tests()