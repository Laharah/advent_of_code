import itertools
import re
from collections import defaultdict
from common import Input
from my_utils.graphs import astar_search, cityblock_distance, neighbors4
import functools

SIZE, USED, AVAIL = (0, 1, 2)


def parse(data):
    data.readline()
    data.readline()
    grid = {}
    pairs = defaultdict(set)
    for line in data:
        m = re.findall(r'\d+', line)
        if not m:
            continue
        # print(m)
        x, y, size, used, avail, _ = [int(x) for x in m]
        grid[x, y] = [size, used, avail]

    for (x, y), (_, used, _) in grid.items():
        for (i, j), (_, _, avail) in grid.items():
            if (x, y) == (i, j) or used == 0:
                continue
            if avail >= used:
                pairs[x, y].add((i, j))

    return grid, pairs


def moves_func(grid, state):
    empty, target = state
    transfers = [(x, y) for x, y in neighbors4(empty) if (x, y) in grid]
    for n in transfers:
        if grid[empty][SIZE] > grid[n][USED]:
            yield (n, empty if n == target else target)


def heur_func(state):
    _, target = state
    return cityblock_distance(target)


if __name__ == '__main__':
    grid, pairs = parse(Input(22))
    print(sum(len(s) for s in pairs.values()))
    empty = [n for n in grid if grid[n][USED] == 0][0]
    moves_func = functools.partial(moves_func, grid)
    maxx = max(n[0] for n in grid)
    start = (empty, (maxx, 0))
    path = astar_search(start, heur_func, moves_func=moves_func)
    print(path)
    print(len(path) - 1)
