from common import Input


def make_grid(Input):
    grid = {}
    for r, line in enumerate(Input):
        for c, infected in enumerate(line.strip()):
            if infected == '#':
                grid[(r, c)] = 'i'
    r_center = r // 2 + r % 2
    c_center = c // 2 + c % 2
    return grid, (r_center, c_center)


def burst(pos, grid):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0
    while True:
        try:
            current_sq = grid[pos]
        except KeyError:
            current_sq = 'c'

        if current_sq == 'c':
            current_dir = (current_dir - 1) % 4
            grid[pos] = 'w'
        elif current_sq == 'w':
            grid[pos] = 'i'
        elif current_sq == 'i':
            current_dir = (current_dir + 1) % 4
            grid[pos] = 'f'
        elif current_sq == 'f':
            current_dir = (current_dir + 2) % 4
            del grid[pos]

        yield current_sq
        dr, dc = dirs[current_dir]
        r, c = pos
        pos = (r + dr, c + dc)


if __name__ == '__main__':
    grid, center = make_grid(Input(22))
    flips = 0
    g = burst(center, grid)
    for _ in range(10000000):
        flips += next(g) == 'w'
    print(flips)
