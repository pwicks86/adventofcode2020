from collections import defaultdict
with open("input.txt") as f:
    jolts = [int(l) for l in f.readlines()]
jolts.sort()

routes = {}
routes[0] = 1
for j in jolts:
    routes[j] = routes.get(j-1, 0) + routes.get(j-2, 0) + routes.get(j-3, 0)
print(routes[max(routes.keys())])

