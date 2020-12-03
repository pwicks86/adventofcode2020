import re
with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

badcount = 0
for l in lines:
    m = re.match("(\d+)-(\d+) (\w): (.*)", l)
    if (m):
        minl, maxl, letter, pw = m.groups()
        has_minl = pw[int(minl) - 1] == letter
        has_maxl = pw[int(maxl) - 1] == letter
        badcount += 0 if has_minl ^ has_maxl else 1


print(len(lines) - badcount)
