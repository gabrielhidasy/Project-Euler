maxi = 0
maxii = 0
tmp = 0
for a in range(0,100):
    for b in range(0,100):
        k = a**b
        tmp = 0
        for i in str(k):
            tmp = tmp + int(i)
        if(tmp>maxi):
            maxi = tmp
            maxii = k
print(maxi,maxii)
