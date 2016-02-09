base = 1
while True:
    x1 = sorted(str(base))
    x2 = sorted(str(base * 2))
    x3 = sorted(str(base * 3))
    x4 = sorted(str(base * 4))
    x5 = sorted(str(base * 5))
    x6 = sorted(str(base * 6))

    if x1 == x2 == x3 == x4 == x5 == x6:
        break

    base = base + 1

print(base)
