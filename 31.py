import functools

"""Objective: give change for 200p, with the following coins.
   How many ways there are?
"""


S = [1, 2, 5, 10, 20, 50, 100, 200]


@functools.lru_cache(maxsize=1024)  # Dynamic programming through memoization
def count(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 0:  # needs be checked after n & m, as if n = 0 and m < 0 then it would return 1, which should not be the case.
        return 1
        # Dont use this coin + use this coin and maybe it again
    return count(n, m - 1) + count(n - S[m], m)

print(count(200, len(S) - 1))
