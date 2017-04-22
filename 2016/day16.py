from bitarray import Bitarray

def get_data(size, seed):
    while len(seed) < size:
        b = ~seed
        b.reverse()
        seed.append(0)
        seed += b
    return seed[:size]

def get_checksum(data):
    cs = Bitarray(0)
    i = iter(data)
    for a in i:
        try:
            b = next(i)
        except StopIteration:
            break

        if a == b:
            cs.append(1)
        else:
            cs.append(0)
    # print(cs)
    if len(cs)%2 == 0:
        return get_checksum(cs)
    else:
        return cs

if __name__ == '__main__':
    data = get_data(35651584, Bitarray('11100010111110100'))
    print('should be 01010001101011001')
    print(get_checksum(data))
