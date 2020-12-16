from collections import defaultdict, deque
with open("input.txt") as f:
    data = [int(x) for x in f.read().split(",")]

nums = {n:1 for n in data}
spoken_turn = {n:deque([i + 1], 2) for i,n in enumerate(data)}
nums = defaultdict(int, nums)
turn_num = len(nums) + 1
spoken = data[-1]
while True:
    if nums[spoken] == 1:
        spoken = 0
    else:
        spoken = abs(spoken_turn[spoken][0] - spoken_turn[spoken][1])
    if spoken not in spoken_turn:
        spoken_turn[spoken] = deque([],2)
    spoken_turn[spoken].append(turn_num)
    nums[spoken] += 1
    if (turn_num == 2020):
        print(spoken)
        break
    turn_num += 1
