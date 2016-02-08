# Classic way to make dynamic programming

import numpy
matrix = open("p081_matrix.txt").read().split()
paths = numpy.zeros((81, 81), dtype=int)
costs = numpy.zeros((81, 81), dtype=int)
for i in range(2, 81):
    costs[0][i] = costs[i][0] = 1000000000000
for i in range(0, len(matrix)):
    line = matrix[i].split(",")
    for y in range(len(line)):
        paths[i + 1][y + 1] = int(line[y])
for i in range(1, 81):
    for y in range(1, 81):
        costs[i][y] = min(costs[i - 1][y] + paths[i][y],
                          costs[i][y - 1] + paths[i][y])
print(costs[80][80])
