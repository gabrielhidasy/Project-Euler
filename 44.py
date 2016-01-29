def find_pent(n):
    return n*(3*n-1)/2
# = (3n^2-n)/2
pent_inv = {}
for a in range(1,20000000):
    pent_inv[find_pent(a)] = a

minimum = 10000000000000
minimum_x_y = (0,0)
for a in range(1,3000):
    for b in range(1,3000):
        try:
            fpa = find_pent(a)
            fpb = find_pent(b)
            k = pent_inv[fpa+fpb]
            y = pent_inv[fpa-fpb]
            if(abs(fpa-fpb)<minimum):
                minimum = abs(fpa-fpb)
                minimum_x_y = (a,b)
        except:
            continue
print(find_pent(7000))
print(minimum,minimum_x_y)
