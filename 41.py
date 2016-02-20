# Pandigital primes
# Make all primes up to 987654321 seems possible, then just check if
# pandigital
# But I cant make a sieve so large, so I wall go up to sqrt of it and check the
# pandigitals on the fly
# But wait, sum(1..8) = 36, so all are divisible by 3
# The same apply for 9, so we can check up to only 1234567
# Also 12345 -> 15, not good
# 123456 = 21, also not usefull
# Only 7 remains
# Generating all primes up to 7654321 is viable, the code took 4.408s
# Incredibly by generating less numbers (up to 2770) it took 0.245s (and the sieve
# is always under 0.1s)

# One of this rare python beats pypy problems
import itertools


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [1] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            for y in range(2, n):
                try:
                    sieve[i * y] = 0
                except:
                    break
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

prime_list = primes(2770)


max_prime = 2
nl = range(1, 8)
print(nl)
perms = itertools.permutations(nl)
for index, perm in enumerate(perms):
    number = 0
    for i in range(len(perm)):
        number = number + perm[i]
        number = number * 10
    number = number / 10
    if number < prime_list[-1]:
        if number > max_prime and number in prime_list:
            max_prime = number
    else:
        flag = 1
        for divisor in prime_list:
            if number % divisor == 0:
                flag = 0
                break
        if flag:
            if number > max_prime:
                max_prime = number
print(max_prime)
