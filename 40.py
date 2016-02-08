number = ''.join([str(x) for x in range(0, 1000000)])
acc = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    acc = acc * int(number[i])
print(acc)
