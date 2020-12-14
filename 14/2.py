from itertools import chain, combinations
import re 
with open("input.txt") as f:
    lines = f.readlines()

def all_subsets(ss):
    return list(chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1))))

def find_ch(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

memory = {}

mask = ""
masks = []
onemask = 0
x_locs = []

for line in lines:
    cmd, _, arg, eqval = re.match(r"(mask|mem)(\[(\d+)\])? = (.*)", line).groups()
    if cmd == "mask":
        masks.clear()
        mask = eqval.strip()
        onemask = int(eqval.replace("X","0"), 2)
        x_locs = find_ch(mask, "X")
    if cmd == "mem":
        val = int(eqval)
        addr = int(arg)
        addr = onemask | addr
        for subset in all_subsets(x_locs):
            addr_list = list(format(addr, '036b'))
            for loc in x_locs:
                addr_list[loc] = "0"
            # set everything in the subset to one
            for s in subset:
                addr_list[s] = "1"
            memory[int("".join(addr_list), 2)] = val

print(sum(memory.values()))