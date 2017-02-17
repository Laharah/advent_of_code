from common import input
from itertools import combinations
from functools import reduce

total = 0
ribbon = 0
mul = lambda s: reduce(lambda x, y: x * y, s)
for l, w, h in (map(int, line.split('x')) for line in input(2)):
    sides = list(map(mul, combinations((l, w, h), 2)))
    total += sum(sides) * 2 + min(sides)
    perim_smallest = min((a + b) * 2 for a, b in combinations((l, w, h), 2))
    vol = mul((l, w, h))
    ribbon += perim_smallest + vol
print(total, ribbon)
