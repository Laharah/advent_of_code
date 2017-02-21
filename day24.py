from my_utils.iteration import powerset
from functools import reduce
from itertools import chain
from pprint import pprint
from common import input


test = list(chain(range(1, 6), range(7, 12)))

target = sum(test) // 3


def distribute(items, groups, target=None):
    'distribute items amongs x even valued groups'
    target = sum(items) // groups if not target else target
    s_items = frozenset(items)
    # if groups == 1:
    #     if sum(items) == target:
    #         yield frozenset([frozenset(items)])
    #     return
    if groups == 2:
        for s in powerset(items):
            if sum(s) != target:
                continue
            yield frozenset([frozenset(items)])
            return
    for s in powerset(items):
        if sum(s) != target:
            continue
        for solution in distribute(s_items-set(s), groups -1, target=target):
            yield frozenset([frozenset(s)]) | solution


possibles = set(distribute([int(n) for n in input(24)], 3))
# possibles = set(distribute(test, 3))

for s in possibles:
    print(s)

cleaned = []
for solution in possibles:
    s = []
    for part in solution:
        part = tuple(sorted(part))
        s.append(part)
    cleaned.append(tuple(sorted(s, key=len)))
cleaned = sorted(cleaned, key=lambda s: tuple(len(p) for p in s))
smallest = len(cleaned[0][0])
cleaned = [s for s in cleaned if len(s[0]) == smallest]
pprint(cleaned)
product = lambda i: reduce(lambda a, b: a*b, i)
print(min(cleaned, key=lambda s: product(s[0])))
