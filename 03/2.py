with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

def count(xstep, ystep):
    x = xstep
    y = ystep
    tree_count = 0
    while y < len(lines):
        if lines[y][x] == "#":
            tree_count += 1
        y += ystep
        x = (x + xstep) % len(lines[1])
    return tree_count

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
counts = []
for s in slopes:
    counts.append(count(s[0], s[1]))

from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
print(prod(counts))

