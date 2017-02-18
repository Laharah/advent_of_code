from common import input
import itertools


def parse(infile):
    return sorted(int(l.strip()) for l in infile)


coins = parse(input(17))
target = 150
total = 0
fewest = len(coins)
num_fewest = 0

for mask in range(1, 1 << len(coins)):
    mask = '{:>0{lc}}'.format(bin(mask)[2:], lc=len(coins))
    if sum(itertools.compress(coins, (int(c) for c in mask))) == target:
        num_containers = sum(int(c) for c in mask)
        if num_containers < fewest:
            num_fewest = 1
            fewest = num_containers
        elif num_containers == fewest:
            num_fewest += 1
        total += 1

def recursive_solution(coins, target):
    if target == 0:
        return 1
    if target < 0:
        return 0

    solutions = 0
    for coin in coins:
        solutions += recursive_solution(coins-{coin}, target-coin)
    return solutions

print(total, fewest, num_fewest)
print(recursive_solution(set(coins), target))
