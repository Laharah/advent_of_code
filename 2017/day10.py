from common import Input
from my_utils.iteration import chunk
from functools import reduce


def knot(d, pos, skip, l):
    if pos + l < len(d):
        d[pos:pos + l] = reversed(d[pos:pos + l])
    else:
        slc = d[pos:] + d[:(pos + l) % len(d)]
        for i, v in enumerate(reversed(slc), pos):
            i %= len(d)
            d[i] = v
    pos += l + skip
    return pos % len(d)


def knot_hash_1(d, lengths):
    current_pos = 0
    for skip, l in enumerate(lengths):
        current_pos = knot(d, current_pos, skip, l)
    return d


def sparse_hash(b):
    d = list(range(256))
    b = [ord(x) for x in b] + [17, 31, 73, 47, 23]
    skip = 0
    current_pos = 0
    for _ in range(64):
        for l in b:
            current_pos = knot(d, current_pos, skip, l)
            skip += 1
    return d


def dense_hash(s):
    d = sparse_hash(s)
    xor = lambda x, y: x ^ y
    blocks = [reduce(xor, c) for c in chunk(d, 16, 0)]
    return ''.join('{:02x}'.format(x) for x in blocks)


if __name__ == '__main__':
    d = list(range(5))
    assert knot_hash_1(d, (3, 4, 1, 5)) == [3, 4, 2, 1, 0]
    d = list(range(256))
    knot_hash_1(d, (int(x) for x in Input(10).read().split(',')))
    print(d[0] * d[1])

    print(dense_hash(Input(10).read().strip()))

    assert dense_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert dense_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
