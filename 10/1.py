from collections import defaultdict
with open("input.txt") as f:
    jolts = [int(l) for l in f.readlines()]
jolts.sort()

diffcount = defaultdict(lambda : 1)
for i in range(len(jolts) - 1):
    a = jolts[i]
    b = jolts[i + 1]
    diff = b - a
    diffcount[diff] += 1
print(diffcount[3] * diffcount[1])