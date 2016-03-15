import math
from utils import func_timer
from special_nums import get_factors

@func_timer
def get_primes(lower,upper):
	"""Gets all the prime numbers between the lower and upper limits provided"""
	primes = [2]
	for i in range(lower,upper):
		if len(get_factors(i)) == 1:
			primes.append(i)

	return primes

@func_timer
def primes_improved(lower,upper):
	"""Reduces the number of operations by checking against prime factors instead of all possible integer factors"""
	primes = [2]
	for i in range(lower,upper):
		top = math.ceil(math.sqrt(i))
		for j in primes:
			if i%j == 0:
				break
			elif i%j != 0 and j<top:
				continue
			else:
				primes.append(i)
				break
	return primes

def prove_powers(n,k):
	"""Prove that n raised to k is the sum of n consecutive odd
	numbers beginning with n raised to k-1 minus n plus 1
	"""
	base = math.pow(n,k-1) -n
	val = 0
	fin = (2*n)
	for i in range(1,fin,2):
		val += base+i

	return val


