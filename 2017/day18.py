from common import Input
from collections import defaultdict, deque
from pprint import pprint


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


def execute(instructions, cout, pid=0, verbose=False):

    reg = defaultdict(int)
    reg['p'] = pid
    reg['pc'] = 0

    def snd(x, y):
        cout.append(reg[x])

    def i_set(x, y):
        reg[x] = y

    def add(x, y):
        reg[x] += y

    def mul(x, y):
        reg[x] *= y

    def mod(x, y):
        reg[x] %= y

    def jgz(x, y):
        if isinstance(x, str):
            x = reg[x]
        if x > 0:
            reg['pc'] += (y - 1)

    ops = {
        'snd': snd,
        'set': i_set,
        'add': add,
        'mul': mul,
        'mod': mod,
        'jgz': jgz,
    }

    instructions = parse(instructions)
    while True:
        if not -1 < reg['pc'] < len(instructions):
            raise ValueError('PC OUT OF SCOPE')
        cmd, x, y = instructions[reg['pc']]
        if verbose:
            print(reg['pc'], cmd, x, y, reg)
        if cmd == 'rcv':
            # print('PID', pid, 'awaiting at line', pc)
            val = yield
            reg[x] = val
        else:
            if isinstance(y, str):
                y = reg[y]
            ops[cmd](x, y)
        reg['pc'] += 1


def run2():
    cout_a, cout_b = deque(), deque()
    a = execute(Input(18), cout_a, pid=0)
    b = execute(Input(18), cout_b, pid=1)
    next(a)
    next(b)
    a_count = b_count = 0
    loop = 0
    while cout_a or cout_b:
        # print((cout_a, cout_b))
        try:
            a.send(cout_b.popleft())
            b_count += 1
        except IndexError as e:
            pass
        try:
            b.send(cout_a.popleft())
            a_count += 1
        except IndexError as e:
            pass
        # print((cout_a, cout_b))
        loop += 1
        if not loop % 10000:
            print(loop, len(cout_a), len(cout_b))

    return a_count, b_count


if __name__ == '__main__':
    print(run2())
