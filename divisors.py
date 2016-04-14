from utils import func_timer

def get_quot_rem(a,b):
	"""
	Given two numbers that are not divisible
	find the highest quotient and reminder that
	expresses them as a = qb+r
	"""
	c = a
	assert a%b != 0
	while c%b != 0:
		c-=1
	quot = c/b
	rem = a-(b*quot)
	return quot, rem
