from common import Input


def parse(data):
    ranges = []
    for line in data:
        start, stop = [int(x) for x in line.strip().split('-')]
        ranges.append((start, stop))
    ranges.sort()
    return ranges


def scan(ranges):
    i = 0
    total = 0
    for start, stop in ranges:
        print(start, stop)
        if i > 4294967295:
            return total
        for ip in range(i, start):
            # if any(st <= ip <= stp for st, stp in ranges):
            #     continue
            print('IP FOUND: ', ip)
            total += 1
        i = stop + 1 if i < stop else i
    return total


if __name__ == '__main__':
    ranges = parse(Input(20))
    print('Found {} IPs.'.format(scan(ranges)))
