"""We will use cube cordinates taken from a diagonal plane at x + y + z = 0
This will give us a constraint that helps with addressing cordinates.
See https://www.redblobgames.com/grids/hexagons/"""

from common import Input

deltas = [(0, 1, -1), (0, -1, 1), (1, 0, -1), (1, -1, 0), (-1, 0, 1), (-1, 1, 0)]
dirs = "n s ne se sw nw".split()
DIR = dict(zip(dirs, deltas))


class HexPoint:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        if isinstance(other, tuple):
            other = HexPoint(*other)
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return self.__class__(x, y, z)

    def __sub__(self, other):
        if isinstance(other, tuple):
            other = HexPoint(*other)
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return self.__class__(x, y, z)

    def __abs__(self):
        x = abs(self.x)
        y = abs(self.y)
        z = abs(self.z)
        return self.__class__(x, y, z)

    def __repr__(self):
        return "HexPoint({s.x}, {s.y}, {s.z})".format(s=self)


def hex_distance(a, b=(0, 0, 0)):
    if not isinstance(a, HexPoint):
        a = HexPoint(*a)
    if not isinstance(b, HexPoint):
        b = HexPoint(*b)
    d = abs(a - b)
    return (d.x + d.y + d.z) // 2


if __name__ == '__main__':
    pos = HexPoint(0, 0, 0)
    furthest = 0
    for d in Input(11).read().strip().split(','):
        pos += DIR[d]
        furthest = max((hex_distance(pos), furthest))
    print(pos)
    print(hex_distance(pos))
    print("Furthest:", furthest)
