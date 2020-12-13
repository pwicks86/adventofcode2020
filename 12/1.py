import re
with open("input.txt") as f:
    lines = f.readlines()

x = 0
y = 0
facing = 90

for line in lines:
    action, num_str = re.match(r"(\w)(\d+)", line.strip()).groups()
    num = int(num_str)
    if action == "F":
        if facing == 0:
            action = "N"
        elif facing == 90:
            action = "E"
        elif facing == 180:
            action = "S"
        else:
            action = "W"
    if action == "N":
        y += num
    elif action == "S":
        y -= num
    elif action == "E":
        x += num
    elif action == "W":
        x -= num
    elif action == "L":
        facing -= num
    elif action == "R":
        facing += num
    facing = facing % 360

print(abs(x) + abs(y))
