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

def distribute3(items):
    'finds every way you can make an evenly distiputable 1/3rd'
    target = sum(items) // 3
    s_items = set(items)
    for way in all_ways(target, items):
        remaining = s_items - way
        # if any(s.issubset(remaining) for s in valid_solutions):
        #     valid_solutions.add(way)
        if any(all_ways(target, remaining)):
            yield way

def all_ways(target, items):
    'yield every set of items that sum to target from items'
    if target == 0:
        yield set()
        return
    if target < 0:
        return
    if not items:
        return
    used = set()
    for coin in items:
        used.add(coin)
        for s in all_ways(target - coin, items - used):
            yield s | {coin}

def running_min(key=None):
    if not key:
        key = lambda i:i
    _min = yield
    yield _min
    k_min = key(_min)
    while True:
        sent = yield
        ks = key(sent)
        if ks < k_min:
            _min = sent
            k_min = ks
        yield _min




product = lambda s: reduce(lambda a,b: a*b, s)
nums = set(int(n) for n in input(24))
# max_l = 0
# for i, w in enumerate(all_ways(sum(nums)//3, nums)):
#     _min = c_min.send(w)
#     if not i%1000:
#         max_l = max(max_l, len(str(w)))
#         print('{:{max_l}} {}'.format(str(w), str(_min), max_l=max_l+1))
# print(f'there are {i} possible solutions')

possibles = distribute3(nums)

c_min = running_min(key=lambda s:(len(s), product(s)))
next(c_min)
max_l = 0
for i, p in enumerate(possibles):
    _min = c_min.send(p)
    if not i%1000:
        max_l = max(max_l, len(str(p)))
        print('{:{max_l}} {}'.format(str(p), str(_min), max_l=max_l+1))
print(f'{i} total solutions')
# possibles = distribute3(set(test))

print('solution: ', _min, product(_min))
