import copy
with open("input.txt") as f:
    seats = f.readlines()

seats = [[char for char in line.strip()] for line in seats]

def step(state):
    new_state = copy.deepcopy(state)
    rows = len(state)
    cols = len(state[0])
    for row in range(rows):
        for col in range(cols):
            occ_count = 0
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    if x == 0 and y == 0:
                        continue
                    check_row = row + x
                    check_col = col + y
                    if 0 <= check_row < rows and 0 <= check_col < cols:
                        occ_count += 1 if state[check_row][check_col] == "#" else 0
            if state[row][col] == "L" and occ_count == 0:
                new_state[row][col] = "#"
            if state[row][col] == "#" and occ_count >= 4:
                new_state[row][col] = "L"
    return new_state

def count_occupied(state):
    occupied = 0
    rows = len(state)
    cols = len(state[0])
    for row in range(rows):
        for col in range(cols):
            if state[row][col] == "#":
                occupied += 1
    return occupied

def to_str(state):
    return "\n".join(["".join(row) for row in state])

cur_state = seats
while True:
    new_state = step(cur_state)
    if to_str(cur_state) == to_str(new_state):
        break
    cur_state = new_state

print(count_occupied(cur_state))
                    
