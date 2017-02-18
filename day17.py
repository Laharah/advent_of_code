from common import input
from collections import Counter
from my_utils.decorators import memo


def parse(infile):
    return sorted(int(l.strip()) for l in infile)


coins = parse(input(17))
target = 150

#test data
# coins = 20, 10, 15, 5, 5
# target = 25

depths = Counter()


def recursive_solution(coinsleft, target, depth=0):
    if target == 0:
        depths[depth] += 1
        return 1
    if target < 0:
        return 0

    solutions = 0
    used = set()
    for coin in coinsleft:
        used.add(coin)
        solutions += recursive_solution(coinsleft - used, target - coin[1], depth + 1)
    return solutions


# we add an identifyer to each coin so duplicate coin values are allowed in a
# single stack
print(recursive_solution(frozenset((i, v) for i, v in enumerate(coins)), target))
print(depths)
