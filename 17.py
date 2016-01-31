string = open("17.txt").read()  # Open the result of the lisp file
string_filtered = ''.join(
    [x for x in string if x != ' ' and x != '-' and x != '\n' and x != '"'])
print(len(string_filtered))
z = [x for x in string_filtered if x not in "abcdefghijklmnopqrstuvwxyz"]
print(z)
