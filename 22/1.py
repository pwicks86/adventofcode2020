# with open("test.txt") as f:
with open("input.txt") as f:
    data = f.read()

p1, p2 = data.split("\n\n")

p1d = list(map(int,p1.splitlines()[1:]))
p2d = list(map(int,p2.splitlines()[1:]))

while len(p1d) > 0 and len(p2d) > 0:
    p1c = p1d.pop(0)
    p2c = p2d.pop(0)
    if p1c > p2c:
        p1d.append(max(p1c, p2c))
        p1d.append(min(p1c,p2c))
    else:
        p2d.append(max(p1c, p2c))
        p2d.append(min(p1c,p2c))

score = 0
winner = p1d if len(p2d) == 0 else p2d
for i, c in enumerate(winner):
    mult = len(winner) - i
    score += mult * c

print(score)