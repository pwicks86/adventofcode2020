import itertools
flatten = itertools.chain.from_iterable

with open("input.txt") as f:
    data = f.readlines()

bag_dict = {}
for line in data:
    bag, contains = line.split("contain")
    bag = bag.replace("bags", "").strip()
    if "no other bags" in contains:
        c_bags = {}
    else:
        c_bags = {b[1].replace("bags", "").replace("bag", "").strip(): int(b[0]) for b in [c.strip().split(" ", 1)
                                            for c in contains.replace(".", "").strip().split(",")]}
    bag_dict[bag] = c_bags

search = ["shiny gold"]
total_bags = 0
while True:
    if(len(search) == 0):
        break
    cur_item = search.pop(0)
    total_bags += sum(bag_dict[cur_item].values())
    search.extend(flatten([[k for n in range(v)] for k,v in bag_dict[cur_item].items()]))

print(total_bags)
