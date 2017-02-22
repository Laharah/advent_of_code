from common import input
import re

class Grid:
    def __init__(self):
        ary =[]
        for i in range(1000):
            ary.append([0]*1000)
        self.ary = ary

    def get_points(self, p1, p2):
        'return inclusive rectangle from p1 to p2'
        x1, y1, x2, y2 = *p1, *p2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                yield i, j

    def toggle(self, p1, p2):
        for x, y in self.get_points(p1, p2):
            self.ary[x][y] += 2

    def turn_on(self, p1, p2):
        for x, y in self.get_points(p1, p2):
            self.ary[x][y] += 1

    def turn_off(self, p1, p2):
        for x, y in self.get_points(p1, p2):
            v = self.ary[x][y]
            if v > 0:
                self.ary[x][y] = v - 1

    def count_on(self):
        return sum(l for ln in self.ary for l in ln)

# turn on 86,413 through 408,518
# toggle 340,102 through 918,558
# turn off 441,642 through 751,889

g = Grid()
for line in input(6):
    cmd, p1, p2 = re.match(r'(^.+) (\d+,\d+) through (\d+,\d+)$', line).groups()
    p1 = tuple(map(int, p1.split(',')))
    p2 = tuple(map(int, p2.split(',')))
    if cmd == 'toggle':
        g.toggle(p1, p2)
    elif cmd == 'turn on':
        g.turn_on(p1, p2)
    elif cmd == 'turn off':
        g.turn_off(p1, p2)
print(g.count_on())
