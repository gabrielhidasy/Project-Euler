cnt = 0
whoare = []
for i in range(1,10000):
    curr = i + int(str(i)[::-1])
    thisis = True
    for y in range(0,51):
        curr_rev = int(str(curr)[::-1])
        if(curr_rev==curr):
            thisis = False
            break
        curr = curr + curr_rev
    if(thisis):
        cnt = cnt + 1
        whoare.append(i)
print(cnt,whoare)
print(cnt)
