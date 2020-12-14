from math import gcd
import math
with open("input.txt") as f:
    data = f.readlines()

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

busses = [(int(b), ind) for ind, b in enumerate(data[1].split(",")) if b != "x"]

base_bus = busses[0]

base_amt = 0
n = 1
mult = base_bus[0]
for bus in busses[1:]:
    while True:
        base_mult = base_amt + mult * n
        if (base_mult + bus[1]) % bus[0] == 0:
            base_amt = base_mult
            mult = lcm(mult, bus[0])
            n = 1
            break
        n += 1
    
print(base_mult)