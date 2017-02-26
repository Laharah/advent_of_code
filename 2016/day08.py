import re
from common import Input
from my_utils.iteration import transpose
from pprint import pprint

OFF, ON = '.', '#'

def make_grid(rows, columns):
    grid = []
    for r in range(rows):
        grid.append([OFF]*columns)
    return grid

def make_rect(x, y, grid):
    for r in range(y):
        grid[r][:x] = [ON]*x
    return grid

def rotate_row(row, offset, grid):
    grid[row] = grid[row][-offset:]+grid[row][:-offset]
    return grid

def rotate_column(column, offset, grid):
    grid = list(map(list, (r for r in transpose(grid))))
    grid = rotate_row(column, offset, grid)
    return list(map(list, (r for r in transpose(grid))))

def interpret_instruction(line, grid):
    if line.startswith('rect'):
        func = make_rect
    elif 'column' in line:
        func = rotate_column
    else:
        func = rotate_row

    args = map(int, re.findall('\d+', line))
    return func(*args, grid)

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

if __name__ == '__main__':
    grid = make_grid(6, 50)
    print_grid(grid)
    for line in Input(8):
        grid = interpret_instruction(line, grid)
        print_grid(grid)
    print(sum(c == ON for row in grid for c in row))
