from utils import func_timer

@func_timer
def factorial_loop(n):
	"""Get the nth factorial using a loop"""
	fact = 1
	i = 1
	while i<=n:
		fact *= i
		i+=1

	return fact 


@func_timer
def factorial_rec(n):
	"""Returns the nth factorial using recursion"""

	if n == 1 or n == 0:
		return 1
	else :
		return n*factorial_rec(n-1)
