total = 1
n = 1
increment = 2
layers = 500
while layers:
    for i in range(4):
        n = n + increment
        total = total + n
    increment = increment + 2
    layers -= 1
print(total)
