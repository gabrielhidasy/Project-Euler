import re

def most_common(lst):
    return max(set(lst), key=lst.count)

def decrypt(txt, passwd):
    z = 0
    r = []
    val_s = 0
    for i in range(len(txt)):
        r.append(chr(txt[i]^passwd[z]))
        val_s += txt[i]^passwd[z]
        z = z+1
        if z == 3:
            z = 0
    return ''.join(r), val_s

in_file = [int (x) for x in open("p059_cipher.txt").read().split(",")]
pa = [in_file[x] for x in range(0, len(in_file),3)]
pb = [in_file[x] for x in range(1, len(in_file),3)]
pc = [in_file[x] for x in range(2, len(in_file),3)]
# Trick, the most common letter in English (and most languages) is ' ', as this
# text is fairly large compared to the key, we can find the key by finding the
# most common letter for each char in the key, and XOR it with ' '
A = most_common(pa)^ord(' ')
B = most_common(pb)^ord(' ')
C = most_common(pc)^ord(' ')
txt, val_s = decrypt(in_file, [A, B, C])
print(txt, val_s)
print(sum([ord(x) for x in txt]))
