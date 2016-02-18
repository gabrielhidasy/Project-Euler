# It would have been smarter to make some more math in this
# I just checked all a*a + b*b = c*c a + b + c = p for p from 0 to 1000
# I could substitute some things so a*a + b*b = (p-a-b)^2,  isolate b, in the end
# we can check only even p's and iterate only over p and b

from multiprocessing import Pool


def calc(beg):
    max_tri = 0
    max_p = 0
    for p in range(beg, beg + 250):
        triangs = 0
        for a in range(1, p):
            for b in range(1, p):
                if a + b > p:
                    break
                for c in range(1, p):
                    if a * a + b * b == c * c:
                        if a + b + c == p:
                            triangs = triangs + 1
        if triangs > max_tri:
            max_tri = triangs
            max_p = p
    return (max_p, max_tri)

pool = Pool(4)
print(pool.map(calc, [0, 250, 500, 750]))
