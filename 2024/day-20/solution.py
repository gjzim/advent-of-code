from collections import deque
from itertools import combinations

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(line) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

def get_start_position():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 'S':
                return row, col

    return None

def get_target_position():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 'E':
                return row, col

    return None

start_row, start_col = get_start_position()
target_row, target_col = get_target_position()

def out_of_bounds(row, col):
    return row < 1 or row >= ROWS - 1 or col < 1 or col >= COLS - 1

def bfs():
    dists = {}
    q = deque([(start_row, start_col, 0)])

    while q:
        row, col, cost = q.popleft()
        if (row, col) in dists or \
            out_of_bounds(row, col) or \
            grid[row][col] == '#':
            continue

        dists[(row, col)] = cost

        if row == target_row and col == target_col:
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q.append((row + dr, col + dc, cost + 1))

    return dists

dists = bfs()
solution1 = 0
solution2 = 0

for p1, p2 in combinations(dists.items(), 2):
    (p1_row, p1_col), p1_dist = p1
    (p2_row, p2_col), p2_dist = p2

    manhattan_dist = abs(p1_row - p2_row) + abs(p1_col - p2_col)
    if manhattan_dist == 2 and abs(p1_dist - p2_dist) - manhattan_dist >= 100:
        solution1 += 1
    if manhattan_dist <= 20 and abs(p1_dist - p2_dist) - manhattan_dist >= 100:
        solution2 += 1

print(solution1)
print(solution2)