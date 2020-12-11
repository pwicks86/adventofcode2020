import copy
with open("input.txt") as f:
    seats = f.readlines()

seats = [[char for char in line.strip()] for line in seats]

def step(state):
    new_state = copy.deepcopy(state)
    rows = len(state)
    cols = len(state[0])
    max_step = max(rows, cols)
    for row in range(rows):
        for col in range(cols):
            occ_count = 0
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    if x == 0 and y == 0:
                        continue
                    for magnitude in range(1, max_step):
                        check_row = row + (x * magnitude)
                        check_col = col + (y * magnitude)
                        if 0 <= check_row < rows and 0 <= check_col < cols:
                            if state[check_row][check_col] == "#":
                                occ_count += 1
                                break
                            if state[check_row][check_col] == "L":
                                break
                        
            if state[row][col] == "L" and occ_count == 0:
                new_state[row][col] = "#"
            if state[row][col] == "#" and occ_count >= 5:
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
    if cur_state == new_state:
        break
    cur_state = new_state

print(count_occupied(cur_state))
                    
