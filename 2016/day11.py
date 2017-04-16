import re
from collections import namedtuple
from itertools import combinations, chain
from pprint import pprint
from common import Input
from my_utils.graphs import astar_search

State = namedtuple('State', 'elevator, floor')

def initalize(data):
    floors = []
    for line in data:
        objs = re.findall(r'\w+ generator|\w+-compatible microchip', line)
        floors.append(frozenset(tuple(x.replace('-compatible', '').split()) for x in objs))

    return State(0, tuple(floors))


def get_moves(state):
    current_floor = state.floor[state.elevator]
    elevator = state.elevator
    symetry_flag = False
    for e in (elevator+1, elevator-1):
        if 0 <= e < len(state.floor):
            for obj in chain(combinations(current_floor, 2), combinations(current_floor,1)):
                if len(obj) == 2:
                    if obj[0][0] == obj[1][0]:
                        if symetry_flag:
                            continue
                        else:
                            symetry_flag = True
                prev_floor = state.floor[state.elevator] - set(obj)
                next_floor = state.floor[e] | set(obj)
                if not valid_floor(prev_floor) or not valid_floor(next_floor):
                    continue
                floors = list(state.floor)
                floors[state.elevator] = prev_floor
                floors[e] = next_floor
                yield State(e, tuple(floors))

def valid_floor(floor):
    chips = [x[0] for x in floor if x[1].startswith('micro')]
    gens = [x[0] for x in floor if x[1].startswith('gen')]
    if gens:
        if chips:
            if any(c not in gens for c in chips):
                return False
    return True

def sum_dist_from_top(state):
    total = 0
    for value, floor in enumerate(reversed(state.floor)):
        total += value*len(floor)
    return total


if __name__ == '__main__':
    start = initalize(Input(11))
    pprint(start)
    path = astar_search(start, h_func=sum_dist_from_top, moves_func=get_moves)
    pprint(path)
    print(len(path)-1, ' steps needed.')
