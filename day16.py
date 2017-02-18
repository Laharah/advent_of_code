from common import input
from pprint import pprint
import operator
import re

# Sue 5: cars: 5, perfumes: 6, akitas: 9

def parse(infile):
    data = {}
    for line in infile:
        line = line.strip()
        name, facts = line.split(': ', 1)
        facts = facts.split(", ")
        # print(facts)
        data[name] = {}
        for f in facts:
            n, v = f.split(': ')
            data[name][n] = int(v)
    return data

def filter_by_property(data, name, cmp, value):
    to_delete = set()
    for sue in data:
        d = data[sue]
        try:
            if not cmp(d[name], value):
                to_delete.add(sue)
        except KeyError:
            pass
    for sue in to_delete:
        del data[sue]
    return data

bounds = """children, EQ, 3
cats, GT, 7
samoyeds, EQ, 2
pomeranians, LT, 3
akitas, EQ, 0
vizslas, EQ, 0
goldfish, LT, 5
trees, GT, 3
cars, EQ, 2
perfumes, EQ, 1"""

data = parse(input(16))
ops = {
    'GT': operator.gt,
    'EQ': operator.eq,
    'LT': operator.lt,
}
for line in bounds.splitlines():
    name, cmp, value = line.split(', ')
    value = int(value)
    cmp = ops[cmp]
    data = filter_by_property(data, name, cmp, value)
pprint(data)
print(len(data))
