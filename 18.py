pyramid = """   75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
pyramid = [[int(x) for x in line.split()] for line in pyramid.split("\n")]
dp_pyramid = [pyramid[0]]

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
print(dp_pyramid)
print(max(dp_pyramid[-1]))
