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

