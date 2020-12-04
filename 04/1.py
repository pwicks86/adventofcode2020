with open("input.txt") as f:
    instr = f.read()

valid = 0
passports = instr.split("\n\n")
for p in passports:
    fields = {d[0]: d[1] for d in [f.split(":") for f in p.split()]}
    if len(fields) == 8:
        valid += 1
    elif len(fields) == 7 and "cid" not in fields:
        valid += 1

print(valid)
