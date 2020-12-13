from math import sqrt, degrees, radians, sin, cos, atan2
import re
with open("input.txt") as f:
    lines = f.readlines()

x = 0
y = 0
wx = 10
wy = 1

for line in lines:
    action, num_str = re.match(r"(\w)(\d+)", line.strip()).groups()
    num = int(num_str)
    if action == "N":
        wy += num
    elif action == "S":
        wy -= num
    elif action == "E":
        wx += num
    elif action == "W":
        wx -= num
    elif action == "L":
        r = sqrt(wx**2 + wy**2)
        theta = atan2(wy,wx)
        theta += radians(num)
        wx = round(r * cos(theta))
        wy = round(r * sin(theta))
    elif action == "R":
        r = sqrt(wx**2 + wy**2)
        theta = atan2(wy,wx)
        theta -= radians(num)
        wx = round(r * cos(theta))
        wy = round(r * sin(theta))
    elif action == "F":
        x += wx * num
        y += wy * num

print(abs(x) + abs(y))
