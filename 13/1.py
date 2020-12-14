with open("input.txt") as f:
    data = f.readlines()

earliest = int(data[0])
busses = [int(b) for b in data[1].split(",") if b != "x"]
rems = []
for bus in busses:
    x, rem = divmod(earliest, float(bus))
    rems.append((x + 1) * bus)
minpos = rems.index(min(rems))
min_bus = busses[minpos]
print(int(min_bus  * (min(rems) - earliest)))