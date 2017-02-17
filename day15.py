import re
from common import input
from functools import reduce
from pprint import pprint


# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
def parse(infile):
    ings = {}
    for line in infile:
        name = line.split(':')[0]
        values = re.findall(r'-?\d+', line)
        ings[name] = list(map(int, values))
    return ings


def ratios(num_ings, total_weight):
    if num_ings == 1:
        yield (total_weight, )
    else:
        for w in range(total_weight + 1):
            for remainder in ratios(num_ings - 1, total_weight - w):
                yield (w, ) + remainder


def calc_score(ingredients, ratio):
    num_attribs = len(next(iter(ingredients.values())))
    attribs = {i: 0 for i in range(num_attribs)}
    for ing, r in zip(ingredients.values(), ratio):
        for i in range(num_attribs):
            attribs[i] += ing[i] * r

    for at in attribs:
        if attribs[at] < 0:
            attribs[at] = 0
    if attribs[num_attribs - 1] != 500:
        return 0
    return reduce(lambda x, y: x * y, list(attribs.values())[:-1])


ingredients = parse(input(15))
pprint(ingredients)
best = 0
for ratio in ratios(len(ingredients), 100):
    score = calc_score(ingredients, ratio)
    if score > best:
        best = score
print(best)
