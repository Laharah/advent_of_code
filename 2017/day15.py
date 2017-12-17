def worker(start_val, factor, mult=1):
    prev = start_val

    while True:
        prev = (prev * factor) % 2147483647
        if prev % mult == 0:
            yield prev


def judge(genA, genB, stop, verbose=False):
    i = 0
    for a, b in zip(genA, genB):
        if i >= stop:
            break
        if verbose:
            print(a, b, sep=': ')
            print(a.to_bytes(4, 'big'), b.to_bytes(4, 'big'), sep=': ')
        if a.to_bytes(4, 'big')[-2:] == b.to_bytes(4, 'big')[-2:]:
            yield True
        else:
            yield False
        i += 1


if __name__ == '__main__':
    a_start, b_start = 277, 349
    a = worker(a_start, 16807, mult=4)
    b = worker(b_start, 48271, mult=8)
    j = judge(a, b, 5000000)
    print(sum(j))
