numbers = []
def fact(x):
    if(x<=1):
        return 1
    if(x==2):
        return 2
    if(x==3):
        return 6
    if(x==4):
        return 24
    if(x==5):
        return 120
    if(x==6):
        return 720
    if(x==7):
        return 5040
    if(x==8):
        return 40320
    if(x==9):
        return 362880

for i in range(3,4000000):
    if(i%100000==0):
        print(i/100000)
    curr = str(i)
    currv = 0
    for y in curr:
        k = int(y)
        currv = currv+fact(k)
    if(currv==i):
        numbers.append(i)
print(numbers,sum(numbers))
