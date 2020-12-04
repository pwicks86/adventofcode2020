import re
with open("input.txt") as f:
    instr = f.read()

valid = 0
passports = instr.split("\n\n")
for p in passports:
    fields = {d[0]: d[1] for d in [f.split(":") for f in p.split()]}
    good = False
    if len(fields) == 8:
        good = True
    elif len(fields) == 7 and "cid" not in fields:
        good = True
    good = good and \
        1920 <= int(fields["byr"]) <= 2002 and \
        2010 <= int(fields["iyr"]) <= 2020 and \
        2020 <= int(fields["eyr"]) <= 2030 and \
        re.match("((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)", fields["hgt"]) and \
        re.match("#([a-f]|[0-9]){6}", fields["hcl"]) and \
        re.match("(amb|blu|brn|gry|grn|hzl|oth)", fields["ecl"]) and \
        re.match("[0-9]{9}$", fields["pid"])

    if good:
        valid += 1


print(valid)
