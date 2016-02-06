def is_abundant(x):
    sum_div = 0
    for k in range(1, int(x / 2 + 1)):
        if x % k == 0:
            sum_div += k
        if sum_div > x:
            return True
    return False
abundants = [x for x in range(1, 28124) if is_abundant(x)]


def can_2_abun(x):
    for abundant in abundants:
        if x - abundant in abundants:
            return True
    return False

sum_of_abuns = sum([x for x in range(1, 28123) if not can_2_abun(x)])
print(sum_of_abuns)
