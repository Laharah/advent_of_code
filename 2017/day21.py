import numpy as np
from common import Input


def make_mapping(Input):
    transforms = {}
    for line in Input:
        a, b = [rule_to_bool_array(x) for x in line.split(' => ')]
        for x in (a, np.fliplr(a)):
            for _ in range(4):
                x = np.rot90(x)
                transforms[x.data.tobytes()] = b
    return transforms


def rule_to_bool_array(rule):
    lines = rule.strip().split('/')
    size = len(lines)
    a = np.array([True if c == '#' else False for c in ''.join(lines)]).reshape(size, -1)
    return a


def transform(art, rules):
    if len(art) % 2 == 0:
        size = (len(art) // 2) * 3
    else:
        size = (len(art) // 3) * 4
    new_chunksize = 3 if len(art) % 2 == 0 else 4
    new = np.zeros((size, size), dtype=bool)
    for art_window, new_window in window_chunks(new_chunksize - 1, len(art)):
        new[new_window] = rules[art[art_window].data.tobytes()]
    return new


def window_chunks(chunk_size, size):
    for i in range(size // chunk_size):
        for j in range(size // chunk_size):
            #yapf: disable
            art_slice = (slice(i * chunk_size, (i + 1) * chunk_size),
                         slice(j * chunk_size, (j + 1) * chunk_size))

            new_slice = (slice(i * (chunk_size + 1), (i + 1) * (chunk_size + 1)),
                         slice(j * (chunk_size + 1), (j + 1) * (chunk_size + 1)))
            #yapf: enable
            yield art_slice, new_slice


def make_art(start, rules, iterations):
    current = start
    for _ in range(iterations):
        new = transform(current, rules)
        current = new
    return current


if __name__ == '__main__':
    start = rule_to_bool_array('.#./..#/###')
    transforms = make_mapping(Input(21))
    art = make_art(start, transforms, 18)
    print(np.sum(art))
