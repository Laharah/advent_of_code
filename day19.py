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
    expansions = set()
    for i, c in enumerate(current):
        for j in range(min((i+15, len(current))), i-1, -1):
            part = current[i:j]
            try:
                expanded = mappings[part]
            except KeyError:
                pass
            else:
                for e in expanded:
                    expansions.add(''.join((current[:i], e, current[i+ len(part):])))

    l = []
    for x in expansions:
        if 'e' in x and x != 'e':
            continue
        else:
            l.append(x)
    return sorted(l, key=len)


def dist_to_goal(goal, current):
    diff = 0
    for a, b in zip(goal, current):
        if a != b:
            diff +=1

    return diff + abs(len(goal)-len(current))

def reverse_mappings(mappings):
    original = mappings
    mappings = {}
    for k, expansions in original.items():
        for e in expansions:
            mappings[e] = k
    return mappings



if __name__ == '__main__':
    mappings, start = parse(input(19))
    print(start)
    #
    # start = 'HOHOHOHHH'
    # mappings = {
    # 'H': {'HO','OH'},
    # 'O': {'HH'},
    # 'e': {'H', 'O'}
    # }

    mappings = reverse_mappings(mappings)
    pprint(mappings)

    # print(get_possible_expansions(mappings, start))

    moves = partial(get_possible_expansions, mappings)


    path = astar_search(start, h_func=bfs('e'), moves_func=moves)
    print(path)
    print(len(path))
