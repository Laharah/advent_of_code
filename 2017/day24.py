import re
from common import Input
from my_utils.decorators import memo

def parse(Input):
    units = frozenset(tuple(map(int, x)) for x in re.findall(r'(\d+)/(\d+)', Input.read()))
    return units


@memo
def search(num, remaining):
    if not remaining:
        return 0

    mx = 0
    for comp in (p for p in remaining if num in p):
        mx = max((mx, sum(comp) + search(comp[comp[0]==num], remaining-{comp})))
    return mx

def get_most_valuable_bridge(components):
    return max(search(c[1], components-{c})+c[1] for c in components if 0 in c)


if __name__ == '__main__':
    components = parse(Input(24))
    print(get_most_valuable_bridge(components))
