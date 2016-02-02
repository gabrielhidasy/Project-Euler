print(sum((i for i in range(1, 1000001, 2) if str(i) == str(
    i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1])))
