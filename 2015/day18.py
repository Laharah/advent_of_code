from common import input
from my_utils import graphs


class Grid:
    def __init__(self, infile=None):
        data = {}
        if infile:
            for row, line in enumerate(infile):
                for col, c in enumerate(line.strip()):
                    data[row, col] = 1 if c == '#' else 0
        self.step = 0
        self.data = data
        self.corners = [(0, 0), (0, 99), (99, 0), (99, 99)]
        for c in self.corners:
            self.data[c] = 1

    def evolve(self):
        new_data = {}
        for point, on in self.data.items():
            active_neigbors = sum(self[p] for p in graphs.neighbors8(point))
            if on:
                if not 2 <= active_neigbors <= 3:
                    new_data[point] = 0
                else:
                    new_data[point] = 1
            else:
                if active_neigbors == 3:
                    new_data[point] = 1
                else:
                    new_data[point] = 0
        for c in self.corners:
            new_data[c] = 1
        self.data = new_data
        self.step += 1

    def __getitem__(self, index):
        try:
            return self.data[index]
        except KeyError:
            return 0

    def __str__(self):
        end = max(self.data)
        rows = []
        for row in range(end[0] + 1):
            r = ''.join('#' if self.data[row, col] else '.' for col in range(end[1] + 1))
            rows.append(r)
        return '\n'.join(rows)


grid = Grid(input(18))
# print(grid.data.items())
for _ in range(100):
    grid.evolve()
    assert all(grid[c] for c in grid.corners)
    print(grid, end='\n\n')

print(sum(grid.data.values()))
