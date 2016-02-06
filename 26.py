import functools


@functools.lru_cache(maxsize=None)
def find_frac(x):
    reccur = []
    used_remainders = {}
    d = 1
    while True:
        if d < x:
            d = 10 * d
            continue
        if d in used_remainders:
            reccur = reccur[reccur.index(int(d / x)):]
            break
        used_remainders[d] = True
        reccur.append(int(d / x))
        d = d % x
        if d == 0:
            reccur = []
            break
    return reccur

max_len = 0
d = 0
for i in range(2, 1001):
    if len(find_frac(i)) > max_len:
        max_len = len(find_frac(i))
        d = i
print(d, max_len)
print(find_frac(6))
