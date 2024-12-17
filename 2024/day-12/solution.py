with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(line) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

def get_dirs():
    return [(-1, 0), (0, 1), (1, 0), (0, -1)]

def neighbor_cells(row, col):
    top = grid[row - 1][col] if row > 0 else '#'
    bottom = grid[row + 1][col] if row < ROWS - 1 else '#'
    left = grid[row][col - 1] if col > 0 else '#'
    right = grid[row][col + 1] if col < COLS - 1 else '#'

    return top, bottom, left, right

def corner_cells(row, col):
    top_left = grid[row - 1][col - 1] if row > 0 and col > 0 else '#'
    top_right = grid[row - 1][col + 1] if row > 0 and col < COLS - 1 else '#'
    bottom_left = grid[row + 1][col - 1] if row < ROWS - 1 and col > 0 else '#'
    bottom_right = grid[row + 1][col + 1] if row < ROWS - 1 and col < COLS - 1 else '#'

    return top_left, top_right, bottom_left, bottom_right

def count_diff_neighbors(row, col):
    return sum(cell != grid[row][col] for cell in neighbor_cells(row, col))

def count_corners(row, col):
    count = 0
    cell = grid[row][col]
    top, bottom, left, right = neighbor_cells(row, col)
    top_left, top_right, bottom_left, bottom_right = corner_cells(row, col)

    # Exterior corner
    count += cell != top and cell != left
    count += cell != left and cell != bottom
    count += cell != bottom and cell != right
    count += cell != right and cell != top

    # Interior corner
    count += cell == top and cell == left and cell != top_left
    count += cell == left and cell == bottom and cell != bottom_left
    count += cell == bottom and cell == right and cell != bottom_right
    count += cell == right and cell == top and cell != top_right

    return count

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

def dfs(row, col, group):
    if out_of_bounds(row, col) or visited[row][col] or group != grid[row][col]:
        return 0, 0, 0

    visited[row][col] = True
    area = 1
    perimeter = count_diff_neighbors(row, col)
    corners = count_corners(row, col)

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        a, p, s = dfs(row + dr, col + dc, grid[row][col])
        area, perimeter, corners = area + a, perimeter + p, corners + s

    return area, perimeter, corners

solution1 = 0
solution2 = 0
for row in range(ROWS):
    for col in range(COLS):
        area, perimeter, corners = dfs(row, col, grid[row][col])
        solution1 += area * perimeter
        solution2 += area * corners

print(solution1)
print(solution2)