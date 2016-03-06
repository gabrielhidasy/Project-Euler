import collections


def prime_factors(n):
    plist = []
    for i in range(2, n + 1):
        while n % i == 0:
            plist.append(i)
            n = n / i
    return collections.Counter(plist)


for i in range(2, 10000):
    a = prime_factors(i)
    b = prime_factors(i + 1)
    c = prime_factors(i + 2)
    if len((a + b).keys()) == 4:
        print(a, i, b, i + 1)
        break
