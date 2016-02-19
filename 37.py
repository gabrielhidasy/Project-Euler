# Trucatable primes
# This primes are composed only of 1, 3, 5, 7, 9 (any even would make
# then non prime when truncating from right)

# A truncatable prime contains another truncatable prime for each
# digit of it

# 3797 is truncatable, there must be one other under 10000 and one under 100 not part
# of it

# At most one 5, if there is a 5 and a 7 there must be 2*7, no [39]*


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

prime_list = primes(1000000)
filtered_prime_list = []
for prime_i in prime_list:
    prime = str(prime_i)
    sp = str(prime)
    if '0' in prime or '4' in prime or '6' in prime or '8' in prime:
        continue
    x = [x for x in sp if x == '5']
    if len(x) > 1:
        continue
    filtered_prime_list.append(int(prime))

more_filters = []
for candidate in filtered_prime_list:
    ltr = candidate
    flag = True
    while ltr:
        if ltr not in prime_list:
            flag = False
            break
        ltr = int(ltr / 10)
        if ltr == 0:
            break
    if not flag:
        continue

    rtl = candidate
    flag = True
    while rtl > 10:
        if rtl not in prime_list:
            flag = False
            break
        rtl = int(str(rtl)[1:])

    if not flag:
        continue

    # Numbers ending in 1 are invalid
    if str(candidate)[-1] in ['1', '4', '6', '8', '9']:
        continue

    more_filters.append(candidate)

more_filters = more_filters[4:]
print(more_filters, sum(more_filters))

# It would have been faster to build the numbers up, all need to start from 2, 3, 5, 7
# Just glue numbers around until its not possible to make a prime anymore
