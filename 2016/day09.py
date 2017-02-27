import re
from common import Input
from my_utils.decorators import trace1

def expand_first(string):
    m = re.search(r'\((\d+)x(\d+)\)', string)
    if not m:
        return '', string
    num_chars, repetitions = [int(x) for x in m.groups()]
    chars = string[m.end():m.end()+num_chars]
    as_is = string[:m.start()]
    remainder = string[m.end()+num_chars:]
    return ''.join((as_is, chars*repetitions)), remainder


def decompress(string):
    parts = []
    while True:
        expanded, remainder = expand_first(string)
        if not expanded:
            parts.append(remainder)
            break
        parts.append(expanded)
        string = remainder
    return ''.join(parts)

def decompress2(string):
    matcher = re.compile(r'\((\d+)x(\d+)\)').match
    length = 0
    i = 0
    while i < len(string):
        m = matcher(string, i)
        if m:
            i = m.end()
            num_chars, repetitions = [int(x) for x in m.groups()]
            length += repetitions * decompress2(string[i:i+num_chars])
            i += num_chars
        else:
            i += 1
            length += 1
    return length



if __name__ == '__main__':
    # assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
    # assert decompress('(6x1)(1x3)A') == '(1x3)A'
    print(decompress2('X(8x2)(3x3)ABCY'))

    print(decompress2(Input(9).read().strip()))
