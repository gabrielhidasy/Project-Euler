# How many n-digit positive numbers exist so that they are also an nth power
# 134.217.728 is 8^9

# 100.000.000.000 is 10^10 (11 digit)
# I think its fair to check all numbers with all exponentials,from 1**1 to 10


def solve():
    n = 0
    for base in range(1, 11):
        for expoent in range(1, 100):
            if len(str(base**expoent)) == expoent:
                n = n + 1
            if len(str(base**expoent)) > expoent:  # wont get smaller
                break
    print(n)
    return n
