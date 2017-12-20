import numpy as np
import re
from common import Input
from my_utils.iteration import groupby


def magnitude(vec):
    # |vec|
    return np.sqrt(np.sum(vec**2))


class Particle:
    def __init__(self, pos, vel, acc, id=0):
        self.pos, self.vel, self.acc = pos, vel, acc
        self.time = 0  # time given in ticks
        self.id = id

    def tick_forward(self, steps=1):
        for _ in range(steps):
            self.vel += self.acc
            self.pos += self.vel
            self.time += 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return 'p={}, v={}, a={}'.format(*map(str, (self.pos, self.vel, self.acc)))


def tick_till_moving_away(particles, prune=True):
    """Will simulate particles unill all particles are moving away from the origin"""
    if prune:
        prune_colisions(particles)
    i = 0
    while any(-p.pos @ p.vel > 0 for p in particles):
        for p in particles:
            p.tick_forward()
        if prune:
            prune_colisions(particles)
        i += 1
    return i


def prune_colisions(particles):
    key = lambda p: tuple(p.pos)
    groups = groupby(particles, key=key)
    for g in groups.values():
        if len(g) > 1:
            particles -= set(g)


def parse_input(inp):
    particles = set()
    for i, line in enumerate(inp):
        parts = re.findall(r'<(.+?)>', line)
        parts = [np.array(list(map(int, p.split(',')))) for p in parts]
        particles.add(Particle(*parts, id=i))
    return particles


def nearest_origin_long_term(particles, prune=True):
    ticks = tick_till_moving_away(particles, prune)
    print('simulated', ticks, 'ticks')

    def key_func(p):  # all manhattan >= |vec| so unnecessary
        """key is a tuple because velocity away from origin will always
        tump position, and acceleration will always trump both for greater t"""
        return magnitude(p.acc), abs(-p.pos @ p.vel), magnitude(p.pos)

    return min(particles, key=key_func)


if __name__ == '__main__':
    particles = parse_input(Input(20))
    p = nearest_origin_long_term(particles, prune=True)
    print(p)
    print('Particle #', p.id, sep='')
    print(len(particles))
