import itertools
from collections import Counter


def incremented_password(seed=None):
    if not seed:
        seed = 'a'
        yield seed
    order = list('abcdefghijklmnopqrstuvwxyz')
    _next = {}
    for i, c in enumerate(order):
        _next[order[i - 1]] = c
    current = list(reversed(seed))
    while True:
        current[0] = _next[current[0]]
        if current[0] == 'a':
            carry = True
        else:
            carry = False
        if carry:
            i = 1
            while carry and i < len(current):
                current[i] = _next[current[i]]
                if current[i] != 'a': carry = False
                i += 1
            if carry:
                current.append('a')
        yield ''.join(reversed(current))


for pswd in incremented_password('vzbxkghb'):
    banned = 'iol'
    no_banned = True
    ascending = False
    pairs = 0
    pairs = 0
    for i, c in enumerate(pswd):
        if c in banned:
            no_banned = False
            break
        o = ord(c)
        try:
            if ord(pswd[i + 1]) == o + 1 and ord(pswd[i + 2]) == o + 2:
                ascending = True
        except IndexError:
            pass

        try:
            if c == pswd[i + 1]:
                pairs += 1
                if c == pswd[i - 1] and c != pswd[i - 2]:
                    pairs -= 1
        except IndexError:
            pass

    if all((no_banned, ascending, pairs > 1)):
        print(pswd)
        exit()
