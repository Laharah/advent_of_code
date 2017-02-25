from hashlib import md5

passwd = ['x'] * 8
i = -1
for _ in range(8):
    while True:
        i += 1
        h = md5(bytes('cxdnnyjw' + str(i), 'UTF8')).hexdigest()
        if h.startswith('00000'):
            try:
                index = h[5]
                index = int(index)
            except ValueError:
                continue
            try:
                if passwd[index] != 'x':
                    continue
            except IndexError:
                continue
            passwd[index] = h[6]
            print('\r', ''.join(passwd), end= '')
            break
