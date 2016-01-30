import functools

@functools.lru_cache(maxsize=1024)
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

fibgen = (fib(x) for x in range(1,100) if fib(x) <= 4000000)
fibpairs = [x for x in fibgen if x%2==0]
print(sum(fibpairs))

