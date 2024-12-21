from collections import deque, defaultdict

with open("input.txt") as f:
    data = f.read().strip()

inputs = data.split("\n")
num_pad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

dir_pad = [
    ["#", "^", "A"],
    ["<", "v", '>']
]

# dirs = ['^', 'v', '<', '>']
# moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dirs = ['<', '^', '>', 'v']
moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def get_min_len_items(items):
    items.sort(key = lambda p: len(p))
    min_len = len(items[0])
    return list(filter(lambda i: len(i) == min_len, items))

def bfs(grid, start, target):
    ROWS, COLS = len(grid), len(grid[0])
    cells = {grid[row][col]: (row, col) for row in range(ROWS) for col in range(COLS)}
    q = deque([(cells[start], '', '*')])
    visited = set()
    paths = []

    def out_of_bounds(row, col):
        return row < 0 or row >= ROWS or col < 0 or col >= COLS

    while q:
        (row, col), path, face = q.popleft()

        if out_of_bounds(row, col) or grid[row][col] == '#' or (row, col, face) in visited:
            continue

        if (row, col) == cells[target]:
            paths.append(path + 'A')
            continue

        visited.add((row, col, face))

        for move, (dr, dc) in enumerate(moves):
            face = dirs[move]
            q.append(((row + dr, col + dc), path + face, face))

    return get_min_len_items(paths)

memo = {}

for start in list(range(10)) + ['A']:
    for target in list(range(10)) + ['A']:
        key = f"{start}::{target}"
        memo[key] = bfs(num_pad, str(start), str(target))

for start in dirs + ['A']:
    for target in dirs + ['A']:
        key = f"{start}::{target}"
        memo[key] = bfs(dir_pad, start, target)

# 029A
# <A^A^^>AvvvA
# v<<A^>>A<A>A<AAv>A^Av<AAA^>A

def get_click_pattern(pattern):
    pattern = 'A' + pattern
    click_patterns = ['']

    for i in range(1, len(pattern)):
        start, target = pattern[i - 1], pattern[i]
        paths = memo[f"{start}::{target}"]

        new_patterns = []
        for click_pattern in click_patterns:
            for path in paths:
                new_patterns.append(click_pattern + path)
        click_patterns = new_patterns

    return get_min_len_items(click_patterns)

solution1 = 0
# for input in inputs:
#     num = int(input[:-1])
#
#     first_patterns = get_click_pattern(input)
#     second_patterns = []
#     for fp in first_patterns:
#         second_patterns.extend(get_click_pattern(fp))
#
#     second_patterns = get_min_len_items(second_patterns)
#
#     final_patterns = []
#     for sp in second_patterns:
#         final_patterns.extend(get_click_pattern(sp))
#     final_patterns = get_min_len_items(final_patterns)
#
#     solution1 += (num * len(final_patterns[0]))

# print(memo)
print(solution1)
for key, value in memo.items():
    print(key, value)