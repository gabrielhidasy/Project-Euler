pbm = open("pbm").read().split()
prime_dict = {}
prime_list = []
for i in pbm:
    prime_dict[int(i)] = True
circ = 0;
print(len(pbm))
def rots(i):
    li = []
    for y in range(0,len(i)):
        li.append(i[y:]+i[:y])
    return li

def is_circ(i):
    #perms nao e pra ser perms, e pra ser rots
    perms = [''.join(p) for p in rots(i)]
#    print(perms)
    try:
        for k in perms:
#            print(k)
            prime_dict[int(k)]
        return True
    except:
        return False

for i in pbm:
    if(is_circ(i)):
        circ = circ + 1
        print(i)
print(is_circ("197"))
print(circ)

