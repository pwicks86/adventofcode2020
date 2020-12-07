from collections import Counter

with open("input.txt") as f:
    data = f.read()

groups = data.split("\n\n")
group_totals = []
for group in groups:
    group_count = Counter()
    for p in group.splitlines():
        group_count += Counter([c for c in p.strip()])


    group_total = 0
    for _, count in group_count.items():
        if count == len(group.splitlines()):
            group_total += 1
    group_totals.append(group_total)

print(sum(group_totals))

