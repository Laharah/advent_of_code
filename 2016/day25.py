import re
import functools
from common import Input
import itertools


def parse_instructions(instruction_set, instructions):
    parsed = []
    for line in instructions:
        m = re.match(r'(\w\w\w) (-?\d+|\w) ?(-?\d+|\w)?$', line)
        if not m:
            print(line)
        inst, *args = m.groups()
        args = [a for a in args if a is not None]
        if inst not in instruction_set:
            raise ValueError('instruction {} not found'.format(inst))
        parsed.append([inst, args])
    return parsed


def execute(register, instruction_set, instructions):
    instructions = parse_instructions(instruction_set, instructions)
    while register['i'] < len(instructions):
        # print(register)
        inst, args = instructions[register['i']]
        # print(inst, *args)
        try:
            if inst == 'tgl':
                instruction_set[inst](*args, instructions, register['i'])
            elif inst == 'out':
                yield from instruction_set[inst](*args)
            else:
                instruction_set[inst](*args)
        except TypeError:
            pass
        register['i'] += 1
    return register


def resolve(reg):
    try:
        return int(reg)
    except ValueError:
        return register[reg]


def verify(output, registers):
    verification_data = itertools.cycle((0, 1))
    recording = set()
    for i, (v, o) in enumerate(zip(verification_data, output)):
        if v != o:
            return False
        state = (serialize(registers), o)
        if state in recording and len(recording) >= 10:
            return True
        recording.add(state)
    return False


def serialize(registers):
    return tuple(registers.items())


if __name__ == '__main__':

    def cpy(x, y):
        register[y] = resolve(x)

    def inc(x):
        register[x] += 1

    def dec(x):
        register[x] -= 1

    def jnz(x, y):
        register['i'] += resolve(y) - 1 if resolve(x) != 0 else 0

    def tgl(x, instructions, self_index):
        index = register['i'] + resolve(x)
        inst, args = instructions[index]

        if inst == 'inc':
            inst = 'dec'
        elif len(args) == 1:
            inst = 'inc'

        if inst == 'jnz':
            inst = 'cpy'
        elif len(args) == 2:
            inst = 'jnz'
        # print(instructions[index], ' at ', index, ' changed to ', [inst, args])
        instructions[index] = [inst, args]

    def out(x):
        yield resolve(x)

    instruction_set = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
        'tgl': tgl,
        'out': out,
    }

    a = 0
    while True:
        register = {
            'a': a,
            'b': 0,
            'c': 0,
            'd': 0,
            'i': 0,
        }

        if verify(execute(register, instruction_set, Input(25)), register):
            print('DONE: ', a)
            break
        a += 1
