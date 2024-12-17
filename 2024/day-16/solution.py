from collections import deque, defaultdict

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

movements = {
    'n': ['w', 'e'],
    's': ['w', 'e'],
    'w': ['n', 's'],
    'e': ['n', 's']
}

def count_best_seats(parents, cost):
    seats = set()
    q = deque([(target_row, target_col, cost)])

    while q:
        row, col, cost = q.popleft()
        seats.add((row, col))
        q.extend(parents[(row, col, cost)])
        del parents[(row, col, cost)]

    return len(seats)

def bfs():
    costs = {}
    q = deque([(start_row, start_col, 'e', 0)])
    result = float('inf')

    while q:
        row, col, face, cost = q.popleft()
        key = f"{row},{col},{face}"

        if grid[row][col] == '#' or (key in costs and costs[key] <= cost):
            continue

        if row == target_row and col == target_col:
            result = min(result, cost)

        costs[key] = cost
        dr, dc = dirs[face]
        q.append((row + dr, col + dc, face, cost + 1))
        parents[(row + dr, col + dc, cost + 1)].append((row, col, cost))
        for n_face in movements[face]:
            parents[(row, col, cost + 1000)].append((row, col, cost))
            q.append((row, col, n_face, cost + 1000))

    return result


parents = defaultdict(list)
solution1 = bfs()
solution2 = count_best_seats(parents, solution1)

print(solution1)
print(solution2)