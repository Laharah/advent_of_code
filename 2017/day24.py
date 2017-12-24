import re
from common import Input
from my_utils.decorators import memo


def parse(Input):
    units = frozenset(
        tuple(map(int, x)) for x in re.findall(r'(\d+)/(\d+)', Input.read()))
    return units


@memo
def search(num, remaining):
    if not remaining:
        return (0, 0, tuple())

    mx = (0, 0, tuple())
    for comp in (p for p in remaining if num in p):
        l, s, b = search(comp[comp[0] == num], remaining - {comp})
        b = b + (comp, )
        l = len(b)
        s = sum(map(sum, b))
        mx = max((mx, (l, s, b)))
    return mx


def get_most_valuable_bridge(components):
    mx = (0, 0, [])
    for c in (x for x in components if 0 in x):
        l, s, b = search(c[1], components - {c})
        b = b + (c, )
        l = len(b)
        s = sum(map(sum, b))
        mx = max((mx, (l, s, b)))
    return mx[0], mx[1], mx[2][::-1]


if __name__ == '__main__':
    components = parse(Input(24))
    l, s, b = get_most_valuable_bridge(components)
    print('Longest Bridge:', b)
    print('LENGTH:', len(b), 'components')
    print('STRENGTH:', s)
