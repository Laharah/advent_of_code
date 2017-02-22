def indexes(a, b):
    while True:
        a -= 1
        b += 1
        if a == 0:
            a, b = b, 1
        yield a, b


def feed_forward(index, value):
    m, mo = 252533, 33554393
    for i in indexes(*index):
        value = m * value % mo
        yield i, value


if __name__ == '__main__':
    desired_index = (2978, 3083)

    for i, (index, value) in enumerate(feed_forward((6, 6), 27995004)):
        if i % 100000 == 0:
            print(index, value)
        if index == (2978, 3083):
            break

    print(index, value)
