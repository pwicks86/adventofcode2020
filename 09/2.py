import sys
from itertools import combinations
with open("input.txt") as f:
    data = [int(l) for l in f.readlines()]

preamble_len = 25
num = 90433990

for i in range(len(data)):
    for j in range(i, len(data)):
        possible = data[i:j]
        poss_sum = sum(possible)
        if (poss_sum == num):
            print(min(possible) + max(possible))
            sys.exit(0)
        elif poss_sum > num:
            break