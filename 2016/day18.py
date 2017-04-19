from common import Input

def cat(*args):
    return ''.join(args)

def generate_row(previous_row):
    row = ['.']
    trap_configs = {
        '^^.',
        '.^^',
        '^..',
        '..^'}

    for i in range(1, len(previous_row)-1):
        old = previous_row[i-1:i+2]
        assert len(old) == 3
        if old in trap_configs:
            row.append('^')
        else:
            row.append('.')
    row.append('.')
    return ''.join(row)

if __name__ == '__main__':
    num_rows = 1
    last_row = '.' + Input(18).read()[:-1] + '.'
    total = last_row.count('.') - 2
    while num_rows < 400000:
        last_row = generate_row(last_row)
        total += last_row.count('.') -2
        num_rows += 1
        # print(last_row)

print(total)
