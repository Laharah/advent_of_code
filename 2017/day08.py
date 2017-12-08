from common import Input
from collections import defaultdict
import re

comp = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
}

registers = defaultdict(int)

pat = r'^(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (-?\d+)'

highest = 0

for line in Input(8):
    reg, op, v, ca, cmp, cb = re.match(pat, line).groups()
    v, cb = int(v), int(cb)
    ca = registers[ca]
    if not comp[cmp](ca, cb):
        continue
    if op == 'inc':
        v = registers[reg] + v
        highest = max((v, highest))
        registers[reg] = v
    else:
        v = registers[reg] - v
        highest = max((v, highest))
        registers[reg] = v

print(max(registers.items(), key=lambda x: x[1]))
print('highest:', highest)
