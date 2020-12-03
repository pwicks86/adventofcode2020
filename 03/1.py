with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

xstep = 3
ystep = 1
x = xstep
y = ystep
tree_count = 0
while y < len(lines):
    if lines[y][x] == "#":
        tree_count += 1
    y += ystep
    x = (x + xstep) % len(lines[1])

print(tree_count)
