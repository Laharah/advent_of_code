from common import Input
from functools import partial
from my_utils.graphs import astar_search, neighbors4, cityblock_distance

def parse_grid(data):
    grid = {}
    poi = []
    for i, line in enumerate(data):
        for j, c in enumerate(line.strip()):
            grid[j, i] = c
            if c == '0':
                start = (j, i)
            if c not in '#.':
                poi.append(c)
    return grid, start, poi

def moves_func(grid, state):
    location, visited = state
    for p in neighbors4(location):
        v = grid[p]
        if v == '#':
            continue
        if v == '.':
            yield (p, visited)
        else:
            yield (p, visited | {v})

def heur(poi, start, state):
    location, visited = state
    return (len(poi) - len(visited)) + (location != start)

if __name__ == '__main__':
    grid, start_point, goals = parse_grid(Input(24))
    start = (start_point, frozenset('0'))
    moves = partial(moves_func, grid)
    h = partial(heur, goals, start_point)
    p = astar_search(start, h_func=h, moves_func=moves)
    # print(p)
    print(len(p) - 1)
