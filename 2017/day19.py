from common import Input
from my_utils.graphs import neighbors4

DELTAS = set(neighbors4((0, 0)))


def make_maze(txt):
    m = []
    for line in txt:
        m.append(list(line[:-1]))
    return m


def follow_path(maze, pos=None, delta=None):

    if not pos:
        pos = (0, maze[0].index('|'))
    if not delta:
        delta = (1, 0)

    steps = 1
    x, y = pos
    dx, dy = delta
    letters = []
    while maze[x][y] != '+':
        x += dx
        y += dy
        if maze[x][y] == ' ':
            return ''.join(letters), steps
        if maze[x][y] not in '+-|':
            letters.append(maze[x][y])
        steps += 1

    other_dir = DELTAS - {(-dx, -dy)}
    for dx, dy in other_dir:
        if maze[x + dx][y + dy] != ' ':
            x += dx
            y += dy
            let, s = follow_path(maze, (x, y), (dx, dy))
            return ''.join(letters) + let, steps + s


if __name__ == '__main__':
    maze = make_maze(Input(19))
    print(follow_path(maze))
