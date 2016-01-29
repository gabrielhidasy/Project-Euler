# Theorem: A number N can be writen a^x*b^y*c^z where a,b,c are primes
# F(n) (number of divisors) = (x+1)*(y+1)*(z+1)

# So we need to generate the prime factors of a number
import collections

def prime_factors(n):
    plist = []
    for i in range(2, n+1):
        while n%i == 0:
            plist.append(i)
            n = n/i
    return collections.Counter(plist)

def mul(lst):
    acc = 1
    for e in lst:
        acc *= e
    return acc

def num_divisors(n):
    return mul(x+1 for x in n.values())

# A triangle number can be made by AP n*(n+1)/2
# But notice that when n and n+1 are in prime form (return of prime_factors)
# n*n+1 is equal to summing the collections (and expoents)
def triangle(n):
    a = prime_factors(n)
    b = prime_factors(n+1)
    c = a+b # = n*(n+1)
    c[2] -= 1 # = n*(n+1)/2
    return c

i = 0
while(num_divisors(triangle(i)) < 500):
    i = i+1
print(i*(i+1)/2)
