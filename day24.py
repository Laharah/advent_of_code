def distribute(items, groups, target=None):
    'finds every way you can make an evenly distributable subsection'
    target = target if target else sum(items) // groups
    if groups == 1:
        if sum(items) == target:
            yield items
            return
    smallest_len = len(items)
    for way in all_ways(target, items):
        if len(way) > smallest_len:
            continue
        remaining = items - way
        if any(distribute(remaining, groups - 1, target)) and len(way) <= smallest_len:
            smallest_len = len(way)
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
        key = lambda i: i
    _min = yield
    k_min = key(_min)
    while True:
        sent = yield _min
        ks = key(sent)
        if ks < k_min:
            _min = sent
            k_min = ks


if __name__ == '__main__':
    from itertools import chain
    from common import input
    from functools import reduce

    nums = set(int(n) for n in input(24))
    test = set(chain(range(1, 6), range(7, 12)))

    possibles = distribute(nums, 4)
    product = lambda s: reduce(lambda a, b: a * b, s)
    c_min = running_min(key=lambda s: (len(s), product(s)))
    next(c_min)
    max_l = 0
    p_min = 0
    for i, p in enumerate(possibles):
        _min = c_min.send(p)
        if not i % 1000 or p_min != _min:
            max_l = max(max_l, len(str(p)))
            print('{:{max_l}} {}'.format(str(p), str(_min), max_l=max_l + 1))
            p_min = _min
    print('{} total solutions', i)
    print(_min)

    print('solution: ', _min, product(_min))
