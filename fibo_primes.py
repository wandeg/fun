import math
from utils import func_timer
from special_nums import get_factors

def get_primes(lower,upper):
	"""Gets all the prime numbers between the lower and upper limits provided"""
	primes = []
	for i in range(lower,upper):
		if len(get_factors(i)) == 1:
			primes.append(i)

	return primes
print get_primes(3,1000)
assert get_primes(3,7) == [3,5]