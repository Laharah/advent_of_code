import re
from collections import defaultdict
from hashlib import md5
from pprint import pprint

d = defaultdict(set)

keys = []
index = 0
trip = re.compile(r'(\w)\1{2}')
quin = re.compile(r'(\w)\1{4}')
while len(keys) < 64:
    term = 'jlmsuwbz{}'.format(index)
    code = md5(term.encode('utf_8')).hexdigest()
    for _ in range(2016):
        code = md5(code.encode('utf8')).hexdigest()
    q = quin.findall(code)
    for char in q:
        if char in d:
            for s in d[char]:
                if index - s <= 1000:
                    print(code, s, sep=': ')
                    keys.append(s)
            del d[char]
    t = trip.search(code)
    if t:
        # print(code, index, sep=': ')
        t = t.group(1)
        d[t].add(index)

    index += 1
keys = sorted(keys)
print(keys)
print(len(keys))
print(keys[63])
