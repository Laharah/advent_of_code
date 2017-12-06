from common import Input
import itertools

mem = [int(x) for x in Input(6).read().split()]
states = {tuple(mem)}
blocks = len(mem)

for c in itertools.count(1):
    i = max(range(blocks), key=lambda x: mem[x])
    items = mem[i]
    mem[i] = 0
    while items:
        i = (i + 1) % blocks
        mem[i] += 1
        items -= 1
    state = tuple(mem)
    if state in states:
        break
    states.add(state)

print(c)

goal = tuple(mem)

for c in itertools.count(1):
    i = max(range(blocks), key=lambda x: mem[x])
    items = mem[i]
    mem[i] = 0
    while items:
        i = (i + 1) % blocks
        mem[i] += 1
        items -= 1
    state = tuple(mem)
    if state == goal:
        break

print(c)


