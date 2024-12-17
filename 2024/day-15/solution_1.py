from functools import reduce

with open("input.txt") as f:
    data = f.read().strip()

grid_lines, movement_lines = data.split('\n\n')
grid = [list(line) for line in grid_lines.split("\n")]
movements = list(reduce(lambda x, y: x + y, movement_lines.split('\n')))

ROWS, COLS = len(grid), len(grid[0])

def get_start_position():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '@':
                return row, col

    return None

start_row, start_col = get_start_position()

def is_obstacle(row, col):
    return grid[row][col] == '#'

def is_box(row, col):
    return grid[row][col] == 'O'

def is_empty(row, col):
    return grid[row][col] == '.'

def move_boxes_up(row, col):
    empty_cell_row = row
    while empty_cell_row > 0 and is_box(empty_cell_row, col):
        empty_cell_row -= 1

    if is_obstacle(empty_cell_row, col) or empty_cell_row <= 0:
        return

    while empty_cell_row < row:
        grid[empty_cell_row][col] = 'O'
        grid[empty_cell_row + 1][col] = '.'
        empty_cell_row += 1

def move_boxes_down(row, col):
    empty_cell_row = row
    while empty_cell_row < ROWS and is_box(empty_cell_row, col):
        empty_cell_row += 1

    if is_obstacle(empty_cell_row, col) or empty_cell_row >= ROWS:
        return

    while empty_cell_row > row:
        grid[empty_cell_row][col] = 'O'
        grid[empty_cell_row - 1][col] = '.'
        empty_cell_row -= 1

def move_boxes_left(row, col):
    empty_cell_col = col
    while empty_cell_col > 0 and is_box(row, empty_cell_col):
        empty_cell_col -= 1

    if is_obstacle(row, empty_cell_col) or empty_cell_col <= 0:
        return

    while empty_cell_col < col:
        grid[row][empty_cell_col] = 'O'
        grid[row][empty_cell_col + 1] = '.'
        empty_cell_col += 1

def move_boxes_right(row, col):
    empty_cell_col = col
    while empty_cell_col < COLS and is_box(row, empty_cell_col):
        empty_cell_col += 1

    if is_obstacle(row, empty_cell_col) or empty_cell_col >= COLS:
        return

    while empty_cell_col > col:
        grid[row][empty_cell_col] = 'O'
        grid[row][empty_cell_col - 1] = '.'
        empty_cell_col -= 1

def move_boxes(row, col, dir):
    if dir == '^':
        move_boxes_up(row, col)
    elif dir == 'v':
        move_boxes_down(row, col)
    elif dir == '<':
        move_boxes_left(row, col)
    else:
        move_boxes_right(row, col)

def move(row, col, dir):
    new_row, new_col = row, col
    if dir == '^':
        new_row = row - 1
    elif dir == 'v':
        new_row = row + 1
    elif dir == '<':
        new_col = col - 1
    else:
        new_col = col + 1

    if is_obstacle(new_row, new_col):
        return row, col

    if is_box(new_row, new_col):
        move_boxes(new_row, new_col, dir)

    if is_empty(new_row, new_col):
        grid[new_row][new_col] = '@'
        grid[row][col] = '.'
        return new_row, new_col

    return row, col

def get_grid_string():
    output = ''
    for row in grid:
        output += ''.join(row)
        output += '\n'
    output += '\n'
    return output

def print_grid():
    for row in grid:
        print(''.join(row))

def box_gps_coord(row, col):
    return (row * 100) + col

row, col = start_row, start_col
for direction in movements:
    row, col = move(row, col, direction)
print_grid()

solution = 0
for row in range(ROWS):
    for col in range(COLS):
        if is_box(row, col):
            solution += box_gps_coord(row, col)

print(solution)