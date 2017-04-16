from my_utils.graphs import astar_search, neighbors4, cityblock_distance
from collections import deque


def get_moves(point):
    for p in neighbors4(point):
        x, y = p
        if x < 0 or y < 0:
            continue
        o = bin(x * x + 3 * x + 2 * x * y + y + y * y + 1352).count('1') % 2
        if not o:
            yield p


def fill(start, moves_func):
    points = {start}
    paths = deque()
    paths.append([start])
    while paths:
        p = paths.popleft()
        if len(p) <= 50:
            moves = moves_func(p[-1])
            for move in moves:
                if move not in points:
                    points.add(move)
                    paths.append(p[:] + [move])
    return points


if __name__ == '__main__':
    h_func = lambda x: cityblock_distance(x, (31, 39))
    path = astar_search((1, 1), moves_func=get_moves, h_func=h_func)
    print(path)
    print(len(path) - 1)
    points = fill((1, 1), get_moves)
    print(len(points))
