matrix = [[999999999, 99999999999, 999999999, 9999999999, 99999999, 9999999, 999999, 0],
          [0, 131, 673, 235, 103, 18, 0],
          [0, 201, 96, 342, 965, 150, 0],
          [0, 630, 803, 746, 422, 111, 0],
          [0, 537, 699, 497, 121, 956, 0],
          [0, 805, 732, 524, 37, 331, 0],
          [999999999, 99999999999, 999999999, 9999999999, 99999999, 9999999, 99999, 0]]

# We need to find the minimum path from one side to the other
# It can be done with a bit of dynamic programming, or with a
# graph algorithm
min_path = [[99999999999 for z in matrix[x]]
            for x in range(len(matrix))]
for z in range(1, 1000):
    for c in range(1, len(matrix[0]) - 1):
        for l in range(1, len(matrix) - 1):
            try:
                matrix[c][l] = min(matrix[c - 1][l], matrix[c][l - 1],
                                   matrix[c][l + 1]) + matrix[c][l]
            except:
                pass

for line in matrix:
    print(line)
