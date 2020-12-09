from itertools import combinations
with open("input.txt") as f:
    data = [int(l) for l in f.readlines()]

preamble_len = 25

for i in range(25, len(data)):
    possibles = combinations(data[i-preamble_len:i],2)
    good = False
    for p in possibles:
        if p[0] + p[1] == data[i]:
            good = True
            break
    if not good:
        print(data[i])
        break
