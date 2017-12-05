from common import Input

data = [int(x) for x in Input(5)]

i = 0
counter = 0

try:
    while i > -1:
        if data[i] < 3:
            data[i] += 1
            i += data[i] - 1
        else:
            data[i] -= 1
            i += data[i] + 1
        counter += 1
except IndexError:
    print(counter)
