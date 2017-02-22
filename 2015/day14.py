import re
from collections import namedtuple
from common import input
from pprint import pprint
reindeer_stats = namedtuple('reindeer_stats', 'name, speed, fly_time, rest_time')


def parse(infile):
    reindeer = []
    for line in infile:
        # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
        m = re.search(r'^(\w+).*\b(\d+).*\b(\d+).*\b(\d+)', line)
        stats = m.groups()
        stats = (stats[0], *map(int, stats[1:]))
        reindeer.append(reindeer_stats(*stats))
    return reindeer


def get_distance_after_t(r, time=2503):
    flying = True
    distance = 0
    while time > 0:
        if flying:
            chunk = r.fly_time
        else:
            chunk = r.rest_time
        if time < chunk:
            distance += r.speed * time * flying
            time -= time
        else:
            distance += r.speed * chunk * flying
            time -= chunk
        flying = not flying
    return distance


reindeer = parse(input(14))
print('winning distance: ', max(map(get_distance_after_t, reindeer)))
score = {r: 0 for r in reindeer}
for t in range(1, 2504):
    scores = []
    best = 0
    for r in reindeer:
        d = get_distance_after_t(r, t)
        scores.append(d)
        if d > best:
            best = d
    for r, s in zip(reindeer, scores):
        if s == best:
            score[r] += 1

pprint(score)
print(max(score.values()))
