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
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def sequence_primes(n):
    prime_list = primes(n)
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
    
    return max_window, plist, sum(plist)
print(sequence_primes(1000000))
