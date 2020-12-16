import re
with open("input.txt") as f:
    data = f.read()

rules, my_ticket, other_tickets = data.split("\n\n")
rules_dict = {}
for rule in rules.splitlines():
    name, a, b, c, d = re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", rule).groups()
    rule_range = set(range(int(a), int(b) + 1))
    rule_range = rule_range.union(set(range(int(c), int(d)+1)))
    rules_dict[name] = rule_range

def check_valid(ticket):
    invalid_count = 0
    for field in ticket.split(","):
        good = False
        for val in rules_dict.values():
            if int(field) in val:
                good = True
        if not good:
            invalid_count += int(field)
    return invalid_count
    

total_bad_count = 0
for ticket in other_tickets.splitlines()[1:]:
    total_bad_count += check_valid(ticket)

print(total_bad_count)
