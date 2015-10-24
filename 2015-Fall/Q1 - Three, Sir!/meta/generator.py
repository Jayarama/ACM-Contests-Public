from itertools import izip
from itertools import repeat
import random

pairs = []

with open("../tests/small.in") as textfile1, open("../tests/small.out") as textfile2:
    for x, y in izip(textfile1, textfile2):
        x = x.strip()
        y = y.strip()
        #print("{0}\t{1}".format(x, y))
        pairs.append(dict([('in', x), ('out', y)]))

pairs = [x for item in pairs for x in repeat(item, 4)]

random.shuffle(pairs)

xin = open("../tests/large.in", 'w+')
out = open("../tests/large.out", 'w+')

for d in pairs:
    xin.write(d["in"] + "\n")
    out.write(d["out"] + "\n")
