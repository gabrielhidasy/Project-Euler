terms = {}
for a in range(2, 101):
    for b in range(2, 101):
        terms[a**b] = True
print(len(terms))
