from common import Input
import itertools


def distribute_cycle(mem):
    blocks = len(mem)
    while True:
        i = max(range(blocks), key=lambda x: mem[x])
        items = mem[i]
        mem[i] = 0
        while items:
            i = (i + 1) % blocks
            mem[i] += 1
            items -= 1
        yield tuple(mem)


if __name__ == '__main__':

    mem = [int(x) for x in Input(6).read().split()]
    states = {tuple(mem)}

    for c, state in enumerate(distribute_cycle(mem), 1):
        if state in states:
            print(c)
            break
        states.add(state)


    goal = tuple(mem)
    for c, state in enumerate(distribute_cycle(mem), 1):
        if state == goal:
            print(c)
            break

