from collections import deque

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split('\n')
falling_bytes = [list(map(int, line.split(','))) for line in lines]
ROWS, COLS = 71, 71

def fill_grid(bytes):
    grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
    for x, y in bytes:
        grid[x][y] = '#'
    return grid

def print_grid(grid_to_print):
    for row in grid_to_print:
        print(''.join(row))

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

def bfs(grid):
    q = deque([(0, 0, 0)])
    costs = set()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        row, col, cost = q.popleft()
        key = f"{row},{col}"

        if out_of_bounds(row, col) or grid[row][col] == '#' or key in costs:
            continue

        if row == ROWS - 1 and col == COLS - 1:
            return cost

        costs.add(key)

        for dr, dc in dirs:
            q.append((row + dr, col + dc, cost + 1))

    return -1

def find_first_blocking_byte():
    def is_grid_traversable(value):
        return bfs(fill_grid(falling_bytes[:value])) == -1

    left, right = 0, len(falling_bytes) - 1
    while left < right:
        mid = left + (right - left) // 2

        if is_grid_traversable(mid):
            right = mid
        else:
            left = mid + 1

    return falling_bytes[left - 1]

solution1 = bfs(fill_grid(falling_bytes[:1024]))
first_blocking_byte = find_first_blocking_byte()
solution2 = f"{first_blocking_byte[0]},{first_blocking_byte[1]}"

print(solution1)
print(solution2)