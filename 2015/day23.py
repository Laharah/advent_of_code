from common import input
import re
from pprint import pprint


def interpret(instructions):
    reg = {'a': 1, 'b': 0}
    i = 0
    instructions = parse(instructions)

    def hlf(r):
        reg[r] //= 2

    def tpl(r):
        reg[r] *= 3

    def inc(r):
        reg[r] += 1

    def jmp(o):
        nonlocal i
        i += o - 1

    def jie(r, o):
        nonlocal i
        if not reg[r] % 2: i += o - 1

    def jio(r, o):
        nonlocal i
        if reg[r] == 1: i += o - 1

    mapping = {
        'hlf': hlf,
        'tpl': tpl,
        'inc': inc,
        'jmp': jmp,
        'jie': jie,
        'jio': jio,
    }

    pprint(instructions)

    while i < len(instructions):
        cmd, *args = instructions[i]
        print(instructions[i])
        mapping[cmd](*args)
        i += 1
        print(reg, i)

    return reg


def parse(instructions):
    def make_ints(s):
        try:
            return int(s)
        except ValueError:
            return s

    instructions = (re.split(r',?\s', l.strip()) for l in instructions)
    return [tuple(make_ints(p) for p in i) for i in instructions]


if __name__ == '__main__':

    cmds = input(23)

    print(interpret(cmds))
