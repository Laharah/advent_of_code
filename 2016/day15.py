import re
from common import Input


def parse(data):
    disks = []
    for line in data:
        m = re.search(r'#(\d) has (\d+) .* position (\d+)', line)
        num, positions, initial = m.groups()
        disks.append(tuple(int(x) for x in (num, initial, positions)))
    return disks


def get_time(disks):
    t = 0
    while True:
        if all((t + d_num + initial) % positions == 0
               for d_num, initial, positions in disks):
            break
        t += 1
    return t


if __name__ == '__main__':
    disks = parse(Input(15))
    print(get_time(disks))
