from common import Input
import re


def dance(l, instructions):
    l = list(l)

    def rotate_right(steps, *_):
        steps = int(steps)
        beginning, end = l[:-steps], l[-steps:]
        return end + beginning

    def swap_index(i, j):
        i, j = int(i), int(j)
        l[i], l[j] = l[j], l[i]
        return l

    def swap_programs(a, b):
        a, b = l.index(a), l.index(b)
        return swap_index(a, b)

    ops = {'s': rotate_right, 'x': swap_index, 'p': swap_programs}

    for inst in instructions:
        cmd, a, b = inst
        l = ops[cmd](a, b)
    return ''.join(l)


def parse_instructions(instructions):
    parsed = []
    for inst in instructions:
        parsed.append(re.match(r'(\w)([\d|\w]+)/?([\d|\w]+)?', inst).groups())
    return parsed


def multi_dance(dancers, instructions, num_dances):
    cache = {}
    index = {}
    for i in range(num_dances):
        try:
            dancers = cache[dancers]
        except KeyError:
            index[dancers] = i
            ans = dance(dancers, instructions)
            if ans in index:
                print('CYCLE FOUND OF SIZE', index[dancers] - index[ans], 'at index', i)
                print(dancers, '->', ans)
                offset = i + 1
                cycle = 1 + index[dancers] - index[ans]
                print('step', num_dances, 'will be at index',
                      num_dances % (cycle + offset))
                return next(x for x in index if index[x] == num_dances % (cycle + offset))
            cache[dancers] = ans
            dancers = ans

    return dancers


if __name__ == '__main__':
    instructions = Input(16).read().strip().split(',')
    instructions = parse_instructions(instructions)
    final_order = dance('abcdefghijklmnop', instructions)
    print(final_order, '\n')

    print('ANSWER:', multi_dance('abcdefghijklmnop', instructions, 10**9))
