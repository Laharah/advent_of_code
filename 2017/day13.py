from common import Input
from pprint import pprint
from itertools import count


def severity_gen(layers, start_step=0, verbose=False):
    for step in range(max(layers) + 1):
        try:
            width = layers[step]
        except KeyError:
            yield False
            continue

        scanner = get_scanner_pos(width, step + start_step)
        print(step, step + start_step, scanner) if verbose else 0

        if scanner == 0:
            yield True
        else:
            yield False


def get_scanner_pos(width, step):
    period = width + width - 2
    if step % period == 0:
        return 0
    else:
        return -1


def find_min_delay(layers):
    for i in count():
        if not any(severity_gen(layers, i)):
            return i


if __name__ == '__main__':
    layers = dict(tuple(map(int, (line.split(': ')))) for line in Input(13))
    test_layers = {0: 3, 1: 2, 4: 4, 6: 4}
    print(find_min_delay(layers))
