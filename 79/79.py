pwd = open("keylog").read().split()

def test_key(ps):
    for rule in pwd:
        i = 0
        y = 0
        while(i<len(ps) and y < 3):
            if(ps[i]==rule[y]):
                y = y + 1
            i = i + 1
        if(y!=3):
            return False
    return True

for i in range(10000000,100000000):
    if(i%100000==0):
        print(i/100000)
    if(test_key(str(i))):
        print(i)
        break;
print(test_key("73162890"))
