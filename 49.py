primes = []
for i in range(2, 10000):
    flag = 1
    for y in range(2, i):
        if i % y == 0:
            flag = 0
            break
    if flag:
        primes.append(i)
resps = []
for i in range(len(primes)):
    if primes[i] < 1000:
        continue
    j = i + 1
    k = i + 2
    while k < len(primes):
        if primes[k] - primes[j] == primes[j] - primes[i]:
            pa = int(''.join(sorted(str(primes[i]))))
            pb = int(''.join(sorted(str(primes[j]))))
            pc = int(''.join(sorted(str(primes[k]))))
            if pa == pb == pc:
                print('{}{}{}'.format(primes[i], primes[j], primes[k]))
                k = len(primes)
            k = k + 1
            continue
        if primes[k] - primes[j] > primes[j] - primes[i]:
            j = j + 1
            continue
        if primes[k] - primes[j] < primes[j] - primes[i]:
            k = k + 1
            continue
