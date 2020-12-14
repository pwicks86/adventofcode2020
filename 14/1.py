import re
with open("input.txt") as f:
    lines = f.readlines()

memory = {}

onemask = 0
zeromask = 0

for line in lines:
    cmd, _, arg, eqval = re.match(r"(mask|mem)(\[(\d+)\])? = (.*)", line).groups()
    if cmd == "mask":
        onemask = int(eqval.replace("X","0"), 2)
        zeromask = ~int(eqval.replace("1","X").replace("0","1").replace("X","0"), 2)
    if cmd == "mem":
        val = int(eqval)
        val = onemask | val
        memory[int(arg)] = val & zeromask

print(sum(memory.values()))