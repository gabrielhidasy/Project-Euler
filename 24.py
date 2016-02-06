import itertools

perms = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for index, perm in enumerate(perms):
    if index == 1000000 - 1:
        print(perm)
        break
