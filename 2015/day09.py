from common import input
import re
from itertools import permutations

edge = {}
cities = set()

for line in input(9):
    m = re.match(r'^(\w+) to (\w+) = (\d+)$', line)
    a, b, dist = m.groups()
    cities.add(a)
    cities.add(b)
    dist = int(dist)
    edge[a, b] = edge[b, a] = int(dist)

def salesman(longest=False):
    best = float('inf') if not longest else 0
    for p in permutations(cities):
        s = 0
        for i, c in enumerate(p):
            try:
                s += edge[c, p[i+1]]
            except IndexError:
                pass
        if not longest and s < best:
            best = s
        elif longest and s > best:
            best = s
    return best

print('shortest: ', salesman())
print('longest: ', salesman(True))
