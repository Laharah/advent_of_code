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

    def snd(x, y):
        reg['sound'] = reg[x]

    def i_recover(x, y):
        nonlocal recover
        recover = True

    def i_set(x, y):
        reg[x] = y

    def add(x, y):
        reg[x] += y

    def mul(x, y):
        reg[x] *= y

    def mod(x, y):
        reg[x] %= y

    def jgz(x, y):
        nonlocal pc
        pc = pc + (y - 1) if reg[x] else pc

    ops = {
        'rcv': i_recover,
        'snd': snd,
        'rcv': i_recover,
        'set': i_set,
        'add': add,
        'mul': mul,
        'mod': mod,
        'jgz': jgz,
    }

    sound = None
    recover = False
    pc = 0
    instructions = parse(instructions)
    while not recover:
        cmd, x, y = instructions[pc]
        if isinstance(y, str):
            y = reg[y]
        ops[cmd](x, y)
        pc += 1

    return reg['sound']


if __name__ == '__main__':
    print(execute(Input(18)))
