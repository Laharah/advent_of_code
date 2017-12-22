from collections import defaultdict
from common import Input

def make_grid(Input):
    grid = defaultdict(bool)
    for r, line in enumerate(Input):
        for c, infected in enumerate(line.strip()):
            grid[(r,c)] = infected == '#'
    r_center = r//2 + r%2
    c_center = c//2 + c%2
    return grid, (r_center, c_center)


def burst(pos, grid):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0
    while True:
        current_dir = (current_dir + 1)%4 if grid[pos] else (current_dir - 1)%4
        dr, dc = dirs[current_dir]
        r, c = pos
        if not grid[pos]:
            yield True
            grid[pos] = True
        else:
            yield False
            grid[pos] = False
        pos = (r+dr, c+dc)

if __name__ == '__main__':
    grid, center = make_grid(Input(22))
    flips = 0
    g = burst(center, grid)
    for _ in range(10000):
        flips += next(g)
    print(flips)



