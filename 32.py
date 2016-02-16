# Idea, get two numbers, a and b, iterating up to 40000
# (so that a*b goes to 1600000000 > 987654321)
# If their product is pandigital, add to a dict
# Get the dict keys
from multiprocessing import Pool
PROCS = 4


def calc(rang):
    numbers = {}
    print(rang)
    for a in range(rang[0], rang[1]):
        for b in range(4000):
            c = a * b
            if c > 987654321:
                break
            s = [int(x) for x in ('{}{}{}'.format(a, b, c))]
            s.sort()
            # Must be from 1 to 9, that was my mistake
            # if s == range(1, len(s) + 1):
            if s == range(1, 10):
                numbers[c] = True
    return numbers.keys()

pool = Pool(PROCS)
slices = [(x, x + 100) for x in range(0, 2000, 100)]
sols = pool.map(calc, slices)
sols_unified = []
for x in sols:
    for y in x:
        sols_unified.append(y)
sols_unified = set(sols_unified)
print(sols_unified, sum(sols_unified))
