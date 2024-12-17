import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(line) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

def get_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    diagonals_tl_br = []  # Top-left to bottom-right diagonals
    diagonals_tr_bl = []  # Top-right to bottom-left diagonals

    # Top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diagonal = ""
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                diagonal += grid[i][j]
        diagonals_tl_br.append(diagonal)

    # Top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diagonal = ""
        for i in range(rows):
            j = i - d + (cols - 1)
            if 0 <= j < cols:
                diagonal += grid[i][j]
        diagonals_tr_bl.append(diagonal)

    return diagonals_tl_br, diagonals_tr_bl

def transpose_grid(grid):
    return [''.join(col) for col in zip(*grid)]

res = 0
tl_br, tr_bl = get_diagonals(grid)
transposed = transpose_grid(grid)
search_space = tl_br + tr_bl + transposed + lines
print(sum(line.count("XMAS") + line.count("SAMX") for line in search_space))

def get_cell(row, col):
    if row >= ROWS or row < 0 or \
        col >= COLS or col < 0:
        return ''

    return grid[row][col]

def is_cross_mas(row, col):
    lt_br = get_cell(row - 1, col - 1) + grid[row][col] + get_cell(row + 1, col + 1)
    bl_tr = get_cell(row + 1, col - 1) + grid[row][col] + get_cell(row - 1, col + 1)

    return (lt_br == 'MAS' and bl_tr == 'MAS') or \
        (lt_br == 'SAM' and bl_tr == 'SAM') or \
        (lt_br == 'MAS' and bl_tr == 'SAM') or \
        (lt_br == 'SAM' and bl_tr == 'MAS')

# def dfs(row, col, i):
#     if row >= ROWS or row < 0 or \
#         col >= COLS or col < 0 or \
#         i >= 4 or grid[row][col] != target[i]:
#             return 0
#
#     print(grid[row][col], target[i])
#     print(row, col, i)
#     print('------------')
#
#     total = 0
#     for dr in (-1, 0, 1):
#         for dc in (-1, 0, 1):
#             if dr == 0 and dc == 0:
#                 continue
#
#             total += dfs(row + dr, col + dc, i + 1)
#
#     return total
#
solution2 = 0
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == 'A':
            solution2 += is_cross_mas(row, col)
#
print(solution2)