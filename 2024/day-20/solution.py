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

dirs = {
    'n': (-1, 0),
    's': (1, 0),
    'w': (0, -1),
    'e': (0, 1)
}

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

# def bfs():
#     costs = {}
#     q = deque([(start_row, start_col, 'e', 0)])
#     result = float('inf')
#
#     while q:
#         row, col, face, cost = q.popleft()
#         key = f"{row},{col},{face}"
#
#         if grid[row][col] == '#' or (key in costs and costs[key] <= cost):
#             continue
#
#         if row == target_row and col == target_col:
#             result = min(result, cost)
#
#         costs[key] = cost
#         dr, dc = dirs[face]
#         q.append((row + dr, col + dc, face, cost + 1))
#         parents[(row + dr, col + dc, cost + 1)].append((row, col, cost))
#         for n_face in movements[face]:
#             parents[(row, col, cost + 1000)].append((row, col, cost))
#             q.append((row, col, n_face, cost + 1000))
#
#     return result

scores = []
visited = set()
def dfs(row, col, dir, score, power):
    key = f"{row},{col},{dir},{power}"
    if out_of_bounds(row, col) or key in visited or power < 0:
        return

    if row == target_row and col == target_col:
        scores.append(score)
        return

    visited.add(key)

    for n_dir, (dr, dc) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
        n_row, n_col = row + dr, col + dc

        if out_of_bounds(n_row, n_col):
            continue

        dfs(n_row, n_col, n_dir, score + 1, power - (grid[n_row][n_col] == '#'))

def print_grid():
    for row in grid:
        print(''.join(row))

dfs(start_row, start_col, -1, 0, 2)
# print(visited)
print(scores)