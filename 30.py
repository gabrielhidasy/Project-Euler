def tst(n):
    soma = sum([int(x)**5 for x in str(n)])
    if(soma==n):
        return n
    else:
        return 0
acc = 0
for i in range(2,1000000):
    if(i%10000==0):
        print(i/10000)
    acc = acc + tst(i)
print(acc)
