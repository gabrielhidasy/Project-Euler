import sys


def is_reversible(n):
    if n % 10 == 0:
        return False
    for d in str(n + int(str(n)[::-1])):
        if int(d) in [0, 2, 4, 6, 8]:
            return False
    return True
print(sum((is_reversible(x) for x in range(int(sys.argv[1])))))
