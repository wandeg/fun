from utils import func_timer

# @func_timer
def factorial_loop(n, until=1):
	"""Get the nth factorial using a loop"""
	fact = 1
	i = until
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

@func_timer
def n_choose_k_naive(n,k):
	"""
	Returns the number of ways you can choose k 
	items from n items in any order
	"""

	return factorial_loop(n)/(factorial_loop(k)*factorial_loop(n-k))

# @func_timer
def n_choose_k_improved(n,k):
	"""
	Returns the number of ways you can choose k 
	items from n items in any order
	Faster especially if k is close to n
	"""	
	return factorial_loop(n,k+1)/(factorial_loop(n-k))


@func_timer
def pascals_triangle_naive(n):
	"""
	Returns the nth row of pascals triangle the naive way 
	by starting from the first row
	"""
	arr = [1]
	if n == 0:
		return arr
	for i in xrange(0,n):
		arr.insert(0,0)
		arr.append(0)
		nu_arr = []
		for i in xrange(len(arr)-1):
			nu_arr.append(arr[i]+arr[i+1])
		arr = nu_arr

	return nu_arr

@func_timer
def pascals_triangle_binomial(n):
	"""Uses binomial coefficients to generate pascals triangle's nth row"""
	triangle_row = []
	for i in range(n+1):
		triangle_row.append(n_choose_k_improved(n,i))

	return triangle_row

@func_timer
def pascals_triangle_binomial_improved(n):
	"""Uses binomial coefficients to generate pascals triangle's nth row"""
	triangle_row = []
	top = (n/2) + 1
	for i in range(top):
		triangle_row.append(n_choose_k_improved(n,i))
	if n %2 == 0:
		triangle_row.extend(triangle_row[:-1][::-1])
	else:
		triangle_row.extend(triangle_row[::-1])


	return triangle_row
