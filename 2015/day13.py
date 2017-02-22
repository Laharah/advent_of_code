import itertools
import re
from functools import partial

from common import input


def parse():
    guests = set()
    edges = {}
    for line in input(13):
        m = re.match(r'^(\w+).*(lose|gain) (\d+).*\b(\w+).$', line)
        a, sign, amt, b = m.groups()
        amt = int(amt)
        if sign == 'lose':
            amt *= -1
        edges[a, b] = amt
        guests.add(a)
        guests.add(b)
    return guests, edges


def arrangement_value(guests, edges, arrangement):
    total = 0
    for i, g in enumerate(arrangement):
        total += edges[g, arrangement[i - 1]]
        total += edges[arrangement[i - 1], g]
    return total

guests, edges = parse()
for g in guests:
    edges['Me', g] = 0
    edges[g, 'Me'] = 0
guests.add('Me')
best = 0
for arrangement in itertools.permutations(guests):
    value = arrangement_value(guests, edges, arrangement)
    if value > best:
        best = value
print(best)
