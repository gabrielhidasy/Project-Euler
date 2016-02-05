names = open("p022_names.txt").read().split(",")
names.sort()
names = [name[1:-1] for name in names]


def name_score(name):
    return sum([ord(x) - ord('A') + 1 for x in name])

scores = [(index + 1) * name_score(name) for index, name in enumerate(names)]
print(sum(scores))
print(scores[937], names[937])
