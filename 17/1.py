from collections import defaultdict
from copy import copy

with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

row = 0
z = 0
active_cubes = set()
for line in lines:
    col = 0
    for c in line:
        if c == "#":
            active_cubes.add((row,col,z))
        col += 1
    row += 1

def step(state):
    newstate = set()

    min_row = min([k[0] for k in state])
    max_row = max([k[0] for k in state])
    min_col = min([k[1] for k in state])
    max_col = max([k[1] for k in state])
    min_z = min([k[2] for k in state])
    max_z = max([k[2] for k in state])
    for pr in range(min_row - 1, max_row + 2):
        for pc in range(min_col - 1, max_col + 2):
            for pz in range(min_z - 1, max_z + 2):
                pos = (pr,pc,pz)
                active_count = 0
                for r in range(-1,2):
                    for c in range(-1,2):
                        for z in range(-1,2):
                            if r == 0 and c == 0 and z == 0:
                                continue
                            check_pos = tuple(map(lambda i, j: i + j, pos, (r,c,z)))
                            active_count += 1 if check_pos in state else 0
                    
                if pos in state:
                    if active_count == 2 or active_count == 3:
                        # stay active
                        newstate.add(pos)
                if active_count == 3:
                    newstate.add(pos)
    return newstate

for i in range(6):
    active_cubes = step(active_cubes)

print(len(active_cubes))