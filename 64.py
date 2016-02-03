from math import floor


def CFcalc(S):
    if S**(1 / 2) == floor(S**(1 / 2)):
        return [0]  # Tricky, return an odd list to make it fail the even test
    m0 = 0
    d0 = 1
    a0 = floor(S**(1 / 2))
    first_a = a0
    cf = [a0]
    while True:
        m1 = d0 * a0 - m0
        d1 = (S - (m1**2)) / d0
        a1 = floor((first_a + m1) / d1)
        m0 = m1
        d0 = d1
        a0 = a1
        cf.append(a0)
        if a0 == 2 * first_a:
            break
    return cf

print(sum((not(len(CFcalc(x)) % 2) for x in range(10000))))
