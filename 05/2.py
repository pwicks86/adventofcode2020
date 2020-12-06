with open("input.txt") as f:
    data = f.readlines()

ids = []
# Haha, they are just binary numbers
for line in data:
    row_num = int(line[0:7].replace("F", "0").replace("B","1"), 2)
    seat_num = int(line[7:].replace("R", "1").replace("L", "0"), 2)
    seat_id = row_num * 8 + seat_num
    ids.append(seat_id)

ids.sort()
for i in range(len(ids) - 1):
    id_a = ids[i]
    id_b = ids[i + 1]
    if (id_b - id_a) != 1:
        print(id_a + 1)
        break

