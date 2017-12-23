from common import Input
from collections import defaultdict


def parse(instructions):
    inst = []
    for line in instructions:
        cmd, x, *y = line.split()
        y = y[0] if y else None
        try:
            x = int(x)
        except ValueError:
            pass
        try:
            y = int(y)
        except (ValueError, TypeError):
            pass
        inst.append((cmd, x, y))
    return inst


def execute(instructions):

    reg = defaultdict(int)
    reg['pc'] = 0
    reg['mul_count'] = 0

    def i_set(x, y):
        reg[x] = y

    def add(x, y):
        reg[x] += y

    def sub(x, y):
        reg[x] -= y

    def mul(x, y):
        reg[x] *= y
        reg['mul_count'] += 1

    def mod(x, y):
        reg[x] %= y

    def jnz(x, y):
        if isinstance(x, str):
            x = reg[x]
        if x != 0:
            reg['pc'] += (y - 1)

    ops = {
        'set': i_set,
        'add': add,
        'sub': sub,
        'mul': mul,
        'mod': mod,
        'jnz': jnz,
    }

    instructions = parse(instructions)
    while 0 <= reg['pc'] < len(instructions):
        cmd, x, y = instructions[reg['pc']]
        if isinstance(y, str):
            y = reg[y]
        ops[cmd](x, y)
        reg['pc'] += 1
    return reg['mul_count']


if __name__ == '__main__':
    print(execute(Input(23)))
