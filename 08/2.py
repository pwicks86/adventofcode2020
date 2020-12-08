import copy
import re
with open("input.txt") as f:
    lines = f.readlines()

memory = []
for line in lines:
    m = re.match("(\w+) ((\+|-)\d+)", line)
    memory.append(list(m.groups()))

candidates = []
for i in range(len(memory)):
    if memory[i][0] == "jmp" or memory[i][0] == "nop":
        candidate = copy.deepcopy(memory)
        candidate[i][0] = "jmp" if candidate[i][0] == "nop" else "nop"
        candidates.append(candidate)

def exec_prog(prog):
    ip = 0
    acc = 0
    exec_int = set()
    while True:
        if ip in exec_int:
            return False
        if ip == len(prog):
            print(acc)
            return True
        exec_int.add(ip)
        current = prog[ip]
        if current[0] == "acc":
            acc += int(current[1])
            ip += 1
        elif current[0] == "jmp":
            ip += int(current[1])
        elif current[0] == "nop":
            ip += 1

for candidate in candidates:
    if exec_prog(candidate):
        break