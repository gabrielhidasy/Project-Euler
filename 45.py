def find_tri(n):
    return n*(n+1)/2
def find_pen(n):
    return n*(3*n-1)/2
def find_hex(n):
    return n*(2*n-1)

pen_inv = {}
hex_inv = {}
for i in range(1,10000000):
    pen_inv[find_pen(i)] = i
    hex_inv[find_hex(i)] = i

for i in range(1,10000000):
    tri = find_tri(i)
    try:
        pen = pen_inv[tri]
        hexa = hex_inv[tri]
        print(tri,i)
    except:
        continue;
