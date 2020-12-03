import re
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

badcount = 0
for l in lines:
    m = re.match("(\d+)-(\d+) (\w): (.*)", l)
    if (m):
        minl, maxl, letter, pw = m.groups()
        count = pw.count(letter)
        badcount += 0 if count  >= int(minl) and count <= int(maxl) else 1


print(len(lines) - badcount)
