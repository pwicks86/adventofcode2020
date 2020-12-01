from itertools import combinations
f = open("input.txt")
nums = [int(l) for l in f.readlines()]

for combo in combinations(nums, 3):
    if (sum(combo) == 2020):
        print(combo[0] * combo[1] * combo[2])

