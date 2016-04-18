from utils import func_timer

def get_quot_rem(a,b):
	"""
	Given two numbers that are not divisible
	find the highest quotient and reminder that
	expresses them as a = qb+r
	"""
	c = a
	if a%b == 0:
		return a/b, 0
	while c%b != 0:
		c-=1
	quot = c/b
	rem = a-(b*quot)
	return quot, rem

def gcd_naive(a,b):
	"""
	Given 2 positive numbers it returns the gcd
	of the numbers using the remainder through
	repeated ddivision
	"""
	quot, rem = get_quot_rem(a,b)
	if rem == 0:
		return b
	else:
		while rem != 0:
			a = b
			b = rem
			quot, rem = get_quot_rem(a,b)

		return b

def gcd_rec(a,b):
	"""
	Recursively compute the gcd of 2 numbers
	"""
	if a%b ==0:
		return b
	else:
		return gcd_rec(b,a%b)

def divisible_by_six(cap=1000):
	"""
	Assert that all numbers less than cap are 
	divisible by 6 when they form the equation n**3 -n
	"""
	for n in range(cap+1):
		if (n**3 -n) % 6 !=0:
			return n

def divisible_by_thirty(cap=1000):
	"""
	Assert that all numbers less than cap are 
	divisible by 30 when they form the equation n**5 -n
	"""
	for n in range(cap+1):
		if (n**5 -n) % 30 !=0:
			return n



print divisible_by_six()