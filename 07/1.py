with open("input.txt") as f:
    data = f.readlines()

bag_dict = {}
for line in data:
    bag, contains = line.split("contain")
    bag = bag.replace("bags","").strip()
    if "no other bags" in contains:
        c_bags = {}
    else:
        c_bags = {b[1].replace("bags","").replace("bag","").strip(): int(b[0]) for b in [c.strip().split(" ", 1)
                                            for c in contains.replace(".", "").strip().split(",")]}
    bag_dict[bag] = c_bags

gold_count = 0
for bag_name in bag_dict.keys():
    if bag_name == "shiny gold":
        continue
    search = [bag_name]
    while True:
        if(len(search) == 0):
            break
        cur_item = search.pop(0)
        if cur_item == "shiny gold":
            gold_count += 1
            break
        search.extend(list(bag_dict[cur_item].keys()))

print(gold_count)
