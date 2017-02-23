from common import Input
from collections import Counter
import re
from my_utils.strings import grep

def is_real(room):
    checksum = room[-6:-1]
    name, ID = room.rsplit('-', 1)
    c = Counter(name)
    del c['-']
    mc = sorted((n*-1, ch) for ch, n in c.most_common())[:5]
    return ''.join(ch for _, ch in mc) == checksum

def get_id(room):
    return int(re.findall('\d+', room)[0])

def decrypt_name(line):
    name = line.rsplit('-', 1)[0]
    ID = get_id(line)
    offset = ID%26
    mapping = {chr(i+ord('a')):chr(ord('a') + (i+offset)%26) for i in range(0, 27)}
    mapping['-'] = ' '
    trans = str.maketrans(mapping)
    name = name.translate(trans)
    return line, name

if __name__ == '__main__':
    assert is_real('aaaaa-bbb-z-y-x-123[abxyz]')
    assert is_real('a-b-c-d-e-f-g-h-987[abcde]')
    assert is_real('not-a-real-room-404[oarel]')
    assert not is_real('totally-real-room-200[decoy]')

    print(sum(get_id(l) for l in Input(4) if is_real(l.strip())))

    print(decrypt_name('qzmt-zixmtkozy-ivhz-343'))

    for line, name in (decrypt_name(line) for line in Input(4)):
        if 'north' in name:
            print(line, name)
