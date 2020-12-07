with open("input.txt") as f:
    data = f.read()

groups = data.split("\n\n")
a_counts = []
for group in groups:
    a_set = set()
    for p in group:
        for a in p.strip():
            a_set.add(a)
    a_counts.append(len(a_set))

print(sum(a_counts))
