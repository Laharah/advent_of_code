import re
import itertools
from common import Input

def compile_instructions(data):
    patterns = {
        r'rotate (left|right) (\d+) step': rotate,
        r'swap letter (\w) with letter (\w)': swap_letter,
        r'swap position (\d+) with position (\d+)': swap_position,
        r'reverse .+ (\d+)\D*(\d+)': reverse,
        r'rotate based .* (\w)$': rotate_on,
        r'move .* (\d+) to position (\d+)': move,
    }

    instructions=[]
    for line in data:
        for p, func in patterns.items():
            m = re.match(p, line)
            if m:
                instructions.append(func(*m.groups()))
                break
        else:
            raise ValueError('no match for instruction: {}'.format(line))
    return instructions

def rotate(d, new_start):
    new_start = int(new_start)
    if d == 'right':
        new_start = -new_start

    def r(data):
        return data[new_start%len(data):] + data[:new_start%len(data)]
    return r


def swap_letter(a, b):
    def func(data):
        return data.replace(a, '_').replace(b, a).replace('_', b)
    return func

def swap_position(x, y):
    x, y = int(x), int(y)
    def func(data):
        data = list(data)
        data[x], data[y] = data[y], data[x]
        return ''.join(data)
    return func

def reverse(start, stop):
    start, stop = int(start), int(stop)
    'inclusive'
    def func(data):
        data = list(data)
        x = data[start:stop+1]
        x.reverse()
        data[start:stop+1] = x
        return ''.join(data)
    return func

def rotate_on(letter):
    def func(data):
        index = data.index(letter)
        shift = 1+index + (index >= 4)
        return rotate('right', shift)(data)
    return func

def move(x, y):
    x, y = int(x), int(y)
    def func(data):
        data = list(data)
        try:
            l = data.pop(x)
        except IndexError:
            raise
        data.insert(y, l)
        return ''.join(data)
    return func

def execute(data, instructions, verbose=True):
    for i in instructions:
        if verbose:
            print('before: ', data, end='')
        data = i(data)
        if verbose:
            print(' after: ', data)
    return data

if __name__ == '__main__':
    data = 'abcde'
    instructions = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""".splitlines()

    instructions = compile_instructions(instructions)
    ans = execute(data, instructions)
    print(ans)
    assert ans == 'decab'

    instructions = compile_instructions(Input(21))
    data = 'abcdefgh'
    data = execute(data, instructions)
    print(data)

    for p in itertools.permutations('fbgdceah'):
        if execute(p, instructions, verbose=False) == 'fbgdceah':
            print(''.join(p))
            break
