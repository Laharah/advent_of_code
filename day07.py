from common import input
import re
import operator
import string
from pprint import pprint

instructions = {}
original = {}
for line in input(7):
    cmd, wire = line.split(' -> ')
    instructions[wire.strip()] = cmd
    original[wire.strip()] = cmd

def process(wire):
    inst = instructions[wire]
    if isinstance(inst, int):
        print(wire, inst)
        return inst

    else:
        inst = evaluate(inst)
        instructions[wire] = inst
    print(wire, inst)
    return inst


def parse(instruction):
    m = re.match(
        r'^([\d|abcdefghijklmnopqrstuvwxyz]+)? ?(NOT|OR|AND|LSHIFT|RSHIFT)? ?([\d|\w]*)',
        instruction)
    a, op, b = m.groups()
    args = []
    for s in a, b:
        if s:
            if s.isdigit():
                s = int(s)
            args.append(s)

    op_table = {
        'NOT': operator.inv,
        'OR': operator.or_,
        'AND': operator.and_,
        'LSHIFT': operator.lshift,
        'RSHIFT': operator.rshift,
        None: None
    }

    op = op_table[op]

    # print(instruction, (op, args))
    return op, args


def evaluate(instruction):
    op, args = parse(instruction)
    if not op:
        a = args[0]
        if isinstance(a, int):
            return a
        else: return process(a)
    num_args = []
    for a in args:
        if isinstance(a, str):
            a = process(a)
        num_args.append(a)
    return op(*num_args)

pprint(instructions)
b = process('a')

instructions = original
instructions['b'] = b
print(process('a'))
