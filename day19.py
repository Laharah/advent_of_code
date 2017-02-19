from common import input
from my_utils.graphs import astar_search, bfs
from functools import partial
from pprint import pprint


def parse(infile):
    mappings = {}
    line = infile.readline()
    while True:
        if line == '\n':
            break
        symbol, expansion = line.strip().split(' => ')
        try:
            mappings[symbol].add(expansion)
        except KeyError:
            mappings[symbol] = {expansion}
        line = infile.readline()

    goal = infile.readline().strip()

    return mappings, goal


def get_possible_expansions(mappings, current):
    part = ''
    expansions = set()
    for i, c in enumerate(current):
        for j in range(i, min((i+15, len(current)))):
            if part in mappings:
                break
            else:
                part += current[j]
        try:
            expanded = mappings[part]
        except KeyError:
            part = ''
            continue
        for e in expanded:
            expansions.add(''.join((current[:i], e, current[i+ len(part):])))
        part = ''
    return expansions


def dist_to_goal(goal, current):
    if current > goal:
        return 1000000
    diff = 0
    for a, b in zip(goal, current):
        if a != b:
            diff +=1

    return diff + abs(len(goal)-len(current))


if __name__ == '__main__':
    mappings, goal = parse(input(19))
    pprint(mappings)
    print(goal)

    # goal = 'HOHOHO'
    # mappings = {
    # 'H': {'HO','OH'},
    # 'O': {'HH'},
    # 'e': {'H', 'O'}
    # }

    print(len(get_possible_expansions(mappings, goal)))

    dist_to_goal = partial(dist_to_goal, goal)
    moves = partial(get_possible_expansions, mappings)

    def bfestimate(node):
        if len(node) > len(goal):
            return 1000
        elif node == goal:
            return 0
        else:
            return 1

    path = astar_search('e', h_func=bfestimate, moves_func=moves)
    print(path)
    print(len(path))
