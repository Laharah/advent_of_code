from common import Input
from my_utils.graphs import point_from_movement
from my_utils.strings import cat

pad = """
.....
.123.
.456.
.789.
.....
""".split()

pad2 = """
.......
...1...
..234..
.56789.
..ABC..
...D...
.......
""".split()


def translate(instructions, keypad):
    x, y = 3, 1
    d_map = {  # south and north are switched because of row, col difference
        'U': 'S',
        'D': 'N',
        'L': 'W',
        'R': 'E',
    }

    code = []
    for line in instructions:
        for d in line.strip():
            nx, ny = point_from_movement((x, y), d_map[d])
            try:
                if keypad[ny][nx] != '.':
                    x, y = nx, ny
            except IndexError:
                print(ny, nx)
                raise
        code.append(keypad[y][x])
    return cat(code)


if __name__ == '__main__':

    print(translate(Input(2), pad2))
