import fractions


def make_expansion(N):
    base = fractions.Fraction(1, 2)
    for i in range(N):
        base = fractions.Fraction(1, 2 + base)
    return 1 + base

specials = 0
for i in range(1000):
    expansion = make_expansion(i)
    numerator = expansion.numerator
    denominator = expansion.denominator
    if len(str(numerator)) > len(str(denominator)):
        specials += 1

print(specials)
