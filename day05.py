from common import input
from collections import Counter
from pprint import pprint


def cat(*args, sep=''):
    return sep.join(args)


nice = not_nice = 0


def is_nice(s):
    vowels = {c for c in 'aeiou'}
    num_vowels = 0
    banned = set('ab cd pq xy'.split())
    pair = False
    for i, c in enumerate(s):
        if i > 0:
            if s[i - 1:i + 1] in banned:
                return False
            if c == s[i - 1]:
                pair = True
        if c in vowels:
            num_vowels += 1
    return pair and num_vowels >= 3


# print(sum(is_nice(s) for s in input(5)))


def is_nice2(s):
    pair_count = Counter()
    repeat = False
    for i, c in enumerate(s):
        try:
            pair_count[s[i:i + 2]] += 1
            if s[i:i + 3] == c * 3 and s[i:i + 4] != c * 4:
                pair_count[s[i:i + 2]] -= 1
        except IndexError:
            pass
        try:
            if c == s[i + 2]:
                repeat = True
        except IndexError:
            pass

    if repeat and max(pair_count.values()) > 1:
        return True
    else:
        return False


print(sum(is_nice2(s) for s in input(5)))

assert is_nice2('qjhvhtzxzqqjkmpb')
assert is_nice2('xxyxx')
assert not is_nice2('uurcxstgmygtbstg')
assert not is_nice2('ieodomkazucvgmuy')
assert is_nice2('aaaaba')
