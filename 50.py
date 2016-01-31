def primes(n):
    """ Returns  a list of primes < n """
    sieve = [1] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            for y in range(2, n):
                try:
                    sieve[i*y] = 0
                except:
                    break
    return [2] + [i for i in range(3,n,2) if sieve[i]], sieve

def sequence_primes_slow(n):
    prime_list, _ = primes(n)
    prime_list.reverse()
    max_window = 0
    window = 0
    plist = []
    for index, prime in enumerate(prime_list):
        begin = index+1
        end = index+1
        while end < len(prime_list):
            if sum(prime_list[begin:end]) < prime:
                end += 1
            if sum(prime_list[begin:end]) > prime:
                begin += 1
            if sum(prime_list[begin:end]) == prime:
                if end-begin > max_window:
                    max_window = end-begin
                    plist = prime_list[begin:end]
                end = end+1
    return max_window, sum(plist)

def sequence_primes(n):
    prime_list, _ = primes(n)
    max_window = 0
    max_prime = 0
    max_sum = 0
    plist = []
    begin = 0
    for index, prime in enumerate(prime_list):
        begin = index
        end = index
        while True:
            if sum(prime_list[begin:end]) in prime_list:
                if max_window < end-begin:
                    max_window = end-begin
                    max_prime = sum(prime_list[begin:end])
                    plist = prime_list[begin:end]
            end = end + 1
            if end >= len(prime_list) or sum(prime_list[begin:max(begin+max_window, end)]) > prime_list[-1]:
                break
    return max_window, max_prime
for i in range(6, 7):
    print(sequence_primes(10**i))
