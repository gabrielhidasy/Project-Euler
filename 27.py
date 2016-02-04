pbm = open("pbm").read().split()
prime_dict = {}
prime_list = []
for i in pbm:
    prime_dict[int(i)] = True

maxi = 0
maxab = (0,0)

def try_num(a,b):
    k = 0
    trash = 0
    for n in range(0,10000):
        try:
            trash = prime_dict[(n**2)+(a*n)+b]
            k = k + 1
        except:
            return k
    return k

for a in range(-999,1000):
    for b in range(-999,1000):
        seqlen = try_num(a,b)
        if(maxi<seqlen):
            maxi = seqlen
            maxab = (a,b)
print(maxi,maxab,maxab[0]*maxab[1])
