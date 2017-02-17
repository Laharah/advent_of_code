from common import input
from collections import Counter

move_deltas = {
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0),
}

houses = [(0, 0), (0, 0)]

for m in input(3).read():
    try:
        delta = move_deltas[m]
    except KeyError:
        continue
    current = houses[-2]
    x, y = current
    dx, dy = delta
    houses.append((x + dx, y + dy))

c = Counter(houses)
print(len(c))
