import re
with open("input.txt") as f:
    lines = f.readlines()

acc = 0
memory = []
for line in lines:
    m = re.match("(\w+) ((\+|-)\d+)", line)
    memory.append(m.groups())

ip = 0
exec_int = set()
while True:
    if ip in exec_int:
        print(acc)
        break
    exec_int.add(ip)
    current = memory[ip]
    if current[0] == "acc":
        acc += int(current[1])
        ip += 1
    elif current[0] == "jmp":
        ip += int(current[1])
    elif current[0] == "nop":
        ip += 1
