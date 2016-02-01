pyramid = open("p067_triangle.txt").read()
pyramid = pyramid.split("\n")
pyramid = pyramid[:-1]
pyramid = [[int(x) for x in line.split()] for line in pyramid]
dp_pyramid = [pyramid[0]]


def father(x):
    if x == 0:
        return 0
    return (x - 1, x)

for line_num, line in enumerate(pyramid):
    if line_num == 0:
        continue
    new_line = []
    for element_number, element in enumerate(line):
        if element_number == 0:
            new_element = element + dp_pyramid[line_num - 1][element_number]
        elif element_number == len(line) - 1:
            new_element = element + \
                dp_pyramid[line_num - 1][element_number - 1]
        else:
            new_element = element + \
                max(dp_pyramid[line_num - 1][element_number - 1], dp_pyramid[line_num - 1][element_number])
        new_line.append(new_element)
    dp_pyramid.append(new_line)
print(max(dp_pyramid[-1]))
