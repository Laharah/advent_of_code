import re
from common import Input


def has_abba(seq):
    for a, b, c, d in seq_4(seq):
        if a == d != c ==b:
            return True
    return False

def seq_4(seq):
    'Every sequence of 4 letters'
    for i in range(len(seq)-3):
        yield seq[i:i+4]

def is_tls(address):
    sections = re.split(r'\[|\]', address)
    return any(has_abba(s) for s in sections[::2]) and not any(has_abba(s) for s in sections[1::2])

def seq_3(seq):
    for i in range(len(seq)-2):
        yield seq[i:i+3]

def is_aba(seq_of_3):
    return seq_of_3[0] == seq_of_3[2] != seq_of_3[1]

def inverted(aba):
    a, b, _ = aba
    return ''.join((b,a,b))

def is_ssl(address):
    sections = re.split(r'\[|\]', address)
    outs = {s  for sec in sections[::2] for s in seq_3(sec) if is_aba(s)}
    ins  = {s for sec in sections[1::2] for s in seq_3(sec) if is_aba(s)}

    return any(inverted(seq) in ins for seq in outs)

if __name__ == '__main__':
    assert is_tls('abba[mnop]qrst')
    assert not is_tls('aaaa[qwer]tyui')
    assert not is_tls('abcd[bddb]xyyx')
    assert is_tls('ioxxoj[asdfgh]zxcvbn')

    print(sum(is_tls(a) for a in Input(7).read().split()))
    print(sum(is_ssl(a) for a in Input(7).read().split()))
