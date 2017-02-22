from common import Input
import re


def city_dist(point):
    'convert complex cord to cityblock distance'
    return abs(point.real) + abs(point.imag)


def interpret_moves(moves):
    loc, heading = 0, 1j
    visited = {loc}
    for turn, dist in parse(moves):
        heading *= turn
        for _ in range(dist):
            loc += heading
            if loc in visited:
                return city_dist(loc)
            else:
                visited.add(loc)


def parse(text):
    turn = {'R': 1j, 'L': -1j}
    return [(turn[RL], int(dist)) for RL, dist in re.findall(r'([R|L])(\d+)', text)]


print(interpret_moves(input(1).read()))
