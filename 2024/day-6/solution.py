import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(line) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

start_row, start_col = 0, 0
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == '^':
            start_row, start_col = row, col
            break

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

def get_dirs():
    return [(-1, 0), (0, 1), (1, 0), (0, -1)]

def visit_without_modification():
    row, col = start_row, start_col
    dirs, dir = get_dirs(), 0
    cells_visited = set()

    while True:
        dr, dc = dirs[dir]
        next_row, next_col = row + dr, col + dc

        if out_of_bounds(next_row, next_col):
            break

        if grid[next_row][next_col] == '#':
            dir = (dir + 1) % len(dirs)
        else:
            row, col = next_row, next_col
            cells_visited.add((row, col))

    return cells_visited

def has_loop(row = start_row, col = start_col):
    visited = set()
    dirs = get_dirs()
    dir = 0

    while True:
        if (row, col, dir) in visited:
            return True

        dr, dc = dirs[dir]
        next_row, next_col = row + dr, col + dc

        if out_of_bounds(next_row, next_col):
            break

        if grid[next_row][next_col] == '#' or grid[next_row][next_col] == '0':
            dir = (dir + 1) % 4
        else:
            visited.add((row, col, dir))
            row, col = next_row, next_col

    return False

visited_cells = visit_without_modification()
solution1 = len(visited_cells)
solution2 = 0
for row, col in visited_cells:
    if row == start_row and col == start_col:
        continue

    grid[row][col] = '0'
    if has_loop(): solution2 += 1
    grid[row][col] = '.'

print(solution1)
print(solution2)