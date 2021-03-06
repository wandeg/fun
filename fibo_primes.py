import math
from utils import func_timer
from special_nums import get_factors, triangular


@func_timer
def get_primes(lower, upper):
    """Gets all the prime numbers between the lower and upper limits provided"""
    primes = [2]
    for i in xrange(lower, upper):
        if len(get_factors(i)) == 1:
            primes.append(i)

    return primes


@func_timer
def primes_improved(upper, max_count=None):
    """Reduces the number of operations by checking against prime factors instead of all possible integer factors"""
    primes = [2]
    count = 0
    i = 3
    while (count < max_count) or (i < upper):
        top = math.ceil(math.sqrt(i))
        for j in primes:
            if i % j == 0:
                break
            elif i % j != 0 and j < top:
                continue
            else:
                primes.append(i)
                count += 1
                break
        i += 1

    return primes


@func_timer
def primes_between(lower, upper, max_count=None):
    """Reduces the number of operations by checking against prime factors instead of all possible integer factors"""
    primes = primes_improved(upper, max_count)
    idx = 0
    for prime in primes:
        if prime < lower:
            idx += 1
        else:
            break
    return primes[idx:]


def prove_powers(n, k):
    """Prove that n raised to k is the sum of n consecutive odd
    numbers beginning with n raised to k-1 minus n plus 1
    """
    base = math.pow(n, k - 1) - n
    val = 0
    fin = (2 * n)
    for i in xrange(1, fin, 2):
        val += base + i

    return val


def prove_form1():
    """Shows that the first 100 primes greater than 3 are either of the form
            6k + 1 or 6k + 5."""

    primes = primes_between(3, None, 100)
    wanted = []
    for i in primes:
        if i > 3:
            if ((i - 1) % 6) != 0 and ((i - 5) % 6) != 0:
                wanted.append(i)
    return wanted


def get_fibs(n):
    """Gets the first n fibonacci numbers"""
    fib = {1: 1, 2: 1}
    if n >= 3:
        for i in xrange(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

    return fib


def get_nth_fib(n):
    """Returns the nth fibonacci number"""
    fibs = get_fibs(n)
    return fibs[n]


def golden_ratio_fib(n):
    """Use the nth fibonacci number to approximate the golden ratio"""
    fibs = get_fibs(n)
    return fibs[n] / float(fibs[n - 1])


def write_even_using_odd_primes(n):
    """Write a program that finds all the ways to write a given even integer
            n >=6 as the sum of two odd primes"""
    assert n >= 6
    assert n % 2 == 0
    ways = []
    primes = set(primes_improved(n, None))
    top = n / 2
    for prime in primes:
        if prime >= 3 and prime < top:
            partner = n - prime
            if partner in primes:
                ways.append((prime, partner))

    return ways


def fibo_n_sum(n):
    """The first n terms of the Fibonacci sequence satisfy
            u1+u2+u3+...+un = un+2 - 1"""
    checker = get_nth_fib(n + 2) - 1
    fibs = get_fibs(n)
    total = sum(fibs.values())
    return total == checker


def binets(n):
    """Demonstrate Binet's equation to get the nth fibonacci number"""
    return math.floor((1.0 / math.sqrt(5)) * (math.pow((1 + math.sqrt(5)) / 2, n) - math.pow((1 - math.sqrt(5)) / 2, n)))

@func_timer
def sum_equation_naive(a,b,c,d,N):
	total = 0
	for i in xrange(1,N+1):
		y = (a*(i**3))+(b*(i**2))+(c*i)+d
		total+=y

	return total

def sum_first_n_squared(n):
	return (n*(n+1)*((2*n)+1))/6

def sum_first_n_cubed(n):
	return ((n*(n+1))/2)**2

@func_timer
def sum_equation_improved(a,b,c,d,N):
	return a*sum_first_n_cubed(N)+b*sum_first_n_squared(N)+c*triangular(N)+d*N


@func_timer
def palindrome_primes(max_count=None):
    """
    Return a list of pairs of max_count palindrome primes ie
    primes whose reverse are also primes
    """
    primes = [2]
    prime_strings = {'2'}
    count = 0
    i = 3
    palindromes = []
    while (count < max_count):
        top = math.ceil(math.sqrt(i))
        for j in primes:
            if i % j == 0:
                break
            elif i % j != 0 and j < top:
                continue
            else:
                primes.append(i)
                prstr = str(i)
                revstr = prstr[::-1]
                prime_strings.add(prstr)
                if len(prstr) > 1 and revstr in prime_strings and prstr != revstr:
	                count += 1
	                palindromes.append((int(revstr),i))
                break
        i += 1

    return sorted(palindromes)

@func_timer
def goldbachs(n):
    """
    Attempts to prove Goldblach's conjecture that every even
    number is the sum of two primes. This code will do this for
    all even values up to n

    :param n : maximum number up to which we want to prove this
    :returns valid (bool): whether the hypotheses is valid for all 
    even numbers up to n
    """
    valid = True
    primes = set(primes_between(0, n/2 + 1))
    for i in xrange(2,n+1,2):
        for j in xrange(2,(i/2)+1):
            if j in primes and (i-j) in primes:
                valid = valid and True
                break
            else:
                continue
            valid = False

    return valid
