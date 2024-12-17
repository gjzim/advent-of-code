with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(map(int, line)) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

def dfs(row, col, prev, ends = None):
    if row < 0 or row >= ROWS or \
        col < 0 or col >= COLS or \
        grid[row][col] != prev + 1:
        return 0

    if grid[row][col] == 9:
        if ends is not None and (row, col) not in ends:
            ends.add((row, col))
            return 1
        elif ends is None:
            return 1
        else:
            return 0

    return dfs(row + 1, col, grid[row][col], ends) + \
        dfs(row - 1, col, grid[row][col], ends) + \
        dfs(row, col + 1, grid[row][col], ends) + \
        dfs(row, col - 1, grid[row][col], ends)

solution1 = 0
solution2 = 0
for row in range(ROWS):
    for col in range(COLS):
        solution1 += dfs(row, col, -1, set())
        solution2 += dfs(row, col, -1)

print(solution1)
print(solution2)