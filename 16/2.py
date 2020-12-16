from collections import defaultdict
import re
with open("input.txt") as f:
# with open("test2.txt") as f:
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
    

good_tickets = []
for ticket in other_tickets.splitlines()[1:]:
    if check_valid(ticket) == 0:
        good_tickets.append(ticket)

good_tickets.append(my_ticket.splitlines()[1])
good_tickets = [ [int(f) for f in l.split(",")] for l in good_tickets]
my_ticket = good_tickets[-1]

index_to_fields = defaultdict(list)
for i in range(len(good_tickets[0])):
    index_set = set()
    for ticket in good_tickets:
        index_set.add(ticket[i])
    for key, rules_set in rules_dict.items():
        if rules_set.issuperset(index_set):
            index_to_fields[i].append(key)
# while any field has more than one possibliltiy
good_fields = set()
while True:
    for fields in index_to_fields.values():
        if len(fields) == 1 and fields[0] not in good_fields:
            good_field = fields[0]
            good_fields.add(good_field)
            break
    none_to_fix = True
    for k in index_to_fields.keys():
        if len(index_to_fields[k]) > 1:
            none_to_fix = False
            index_to_fields[k].remove(good_field)
    if none_to_fix:
        break

final_val = 1
for k, v in index_to_fields.items():
    if v[0].startswith("departure"):
        final_val *= my_ticket[k]

print(final_val)