import re
import functools
from common import Input


def parse(instruction_set, instructions):
    compiled = []

    for line in instructions:
        m = re.match(r'(\w\w\w) (\d+|\w) ?(-?\d+|\w)?$', line)
        inst, *args = m.groups()
        args = [a for a in args if a is not None]
        if inst not in instruction_set:
            raise ValueError('instruction {} not found'.format(inst))
        compiled.append(functools.partial(instruction_set[inst], *args))
    return compiled


def execute(register, instruction_set, instructions):
    instructions = parse(instruction_set, instructions)
    while register['i'] < len(instructions):
        # print(register)
        try:
            instructions[register['i']]()
        except:
            print(register, instructions[register['i']])
            raise
        register['i'] += 1
    return register


def resolve(reg):
    try:
        return int(reg)
    except ValueError:
        return register[reg]


if __name__ == '__main__':

    def cpy(x, y):
        register[y] = resolve(x)

    def inc(x):
        register[x] += 1

    def dec(x):
        register[x] -= 1

    def jnz(x, y):
        register['i'] += resolve(y) - 1 if resolve(x) != 0 else 0

    instruction_set = {
        'cpy': cpy,
        'inc': inc,
        'dec': dec,
        'jnz': jnz,
    }
    register = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0,
        'i': 0,
        }

    register = execute(register, instruction_set, Input(12))
    print(register)
