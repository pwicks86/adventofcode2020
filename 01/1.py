from itertools import combinations
f = open("input.txt")
nums = [int(l) for l in f.readlines()]

for combo in combinations(nums, 2):
    if (combo[0] + combo[1] == 2020):
        print(combo[0] * combo[1])
