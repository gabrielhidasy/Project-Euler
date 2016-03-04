import itertools
numbers = []
perms = itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for index, perm in enumerate(perms):
    if perm[0] == 0:
        continue
    if perm[3] % 2:
        continue
    if (perm[2] + perm[3] + perm[4]) % 3:
        continue
    if (perm[5] != 0 and perm[5] != 5):
        continue
    if (100 * perm[4] + 10 * perm[5] + perm[6]) % 7:
        continue
    if (100 * perm[5] + 10 * perm[6] + perm[7]) % 11:
        continue
    if (100 * perm[6] + 10 * perm[7] + perm[8]) % 13:
        continue
    if (100 * perm[7] + 10 * perm[8] + perm[9]) % 17:
        continue
    number = 0
    for i in range(10):
        number = number + perm[i]
        number = number * 10
    number = number / 10
    numbers.append(number)

print(sum(numbers))
