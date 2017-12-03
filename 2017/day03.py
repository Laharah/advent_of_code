import math
from my_utils.graphs import cityblock_distance, neighbors8
import numpy as np


def get_cords(N):
    'returns the cordinates of "N" in a spiral graph'
    ring = math.ceil((math.sqrt(N) - 1) / 2)

    side_length = 2 * ring + 1
    ring_max = side_length**2
    side_length -= 1
    side_max = ring_max

    if N >= side_max - side_length:
        return ring - (side_max - N), -ring
    side_max -= side_length

    if N >= side_max - side_length:
        return -ring, -ring + (side_max - N)
    side_max -= side_length

    if N >= side_max - side_length:
        return -ring + (side_max - N), ring

    return ring, ring - (side_max - N - side_length)


def fill_to(grid, N):
    'given a numpy grid, fill in a spiral pattern with neighbors8 sum'
    r, c = len(grid[0]) // 2, len(grid) // 2
    grid[r, c] = 1
    c += 1

    def sum_neighbors(r, c):
        s = sum(grid[y, x] for y, x in neighbors8((r, c)))
        grid[r, c] = s
        return int(s)

    while True:
        #fill up
        while grid[r, c - 1] != 0:
            s = sum_neighbors(r, c)
            if s > N: return s
            r -= 1

        #fill left
        while grid[r + 1, c] != 0:
            s = sum_neighbors(r, c)
            if s > N: return s
            c -= 1

        #fill down
        while grid[r, c + 1] != 0:
            s = sum_neighbors(r, c)
            if s > N: return s
            r += 1

        #fill right
        while grid[r - 1, c] != 0:
            s = sum_neighbors(r, c)
            if s > N: return s
            c += 1


if __name__ == '__main__':
    N = 277678
    print(cityblock_distance(get_cords(N)))
    grid = np.zeros((200, 200))
    print(fill_to(grid, N))
