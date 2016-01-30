import functools

@functools.lru_cache(maxsize=None)
def d(n):
    div_list = []
    for i in range(1, n):
        if n%i == 0:
            div_list.append(i)
    return sum(div_list)

def calculate_pairs():
    # pairs = []
    total = 0
    for i in range(10001):
        if d(i) == 1:
            continue
        for y in range(i, 10001):
            if i == y or d(y) == 1:
                continue
            if d(i) == y and d(y) == i:
                # pairs.append((i,y))
                total += (i + y)
    print(total)

calculate_pairs()
