from my_utils.graphs import astar_search, cityblock_distance, point_from_movement
from hashlib import md5
from pprint import pprint


def get_moves(state, t=True):
    point, path = state
    dirs = md5(path.encode('utf8')).hexdigest()[:4]
    U, D, L, R = dirs
    if not any(d in 'bcdef' for d in (U, D, L, R)):
        if t:
            print('TRAPPED FOREVER: {}'.format(state))
    for door, direction in zip([U, D, L, R], list('UDLR')):
        if door in {'b', 'c', 'd', 'e', 'f'}:
            new_point = point_from_movement(point, direction)
            x, y = new_point
            if 0 <= x < 4 and 0 >= y > -4:
                yield (new_point, path + direction)


def h_func(state):
    point, path = state
    return cityblock_distance(point, q=(3, -3)) * len(path)


def longest_depth_first(state):
    point, path = state
    if point == (3, -3):
        return state, len(path) - 8

    best = None
    for s in get_moves(state, t=False):
        ans = longest_depth_first(s)
        if not ans:
            continue
        p, path_length = ans
        if not best:
            best = p, path_length
        if path_length > best[1]:
            best = (p, path_length)
    return best


if __name__ == '__main__':
    start = ((0, 0), 'bwnlcvfs')
    p = astar_search(start, moves_func=get_moves, h_func=h_func)
    pprint(p)
    print(len(p) - 1)
    print(longest_depth_first(start))
