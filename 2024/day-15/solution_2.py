from functools import reduce

with open("input.txt") as f:
    data = f.read().strip()

grid_lines, movement_lines = data.split('\n\n')

def build_grid(input_grid):
    grid = ['' for _ in range(len(input_grid))]
    for row in range(len(input_grid)):
        for col in range(len(input_grid[0])):
            if input_grid[row][col] == '#':
                grid[row] += '##'
            elif input_grid[row][col] == 'O':
                grid[row] += '[]'
            elif input_grid[row][col] == '@':
                grid[row] += '@.'
            else:
                grid[row] += '..'

        grid[row] = list(grid[row])

    return grid

grid = build_grid([list(line) for line in grid_lines.split("\n")])
movements = list(reduce(lambda x, y: x + y, movement_lines.split('\n')))
ROWS, COLS = len(grid), len(grid[0])

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

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
    return grid[row][col] == '[' or grid[row][col] == ']'

def is_empty(row, col):
    return grid[row][col] == '.'

def move_boxes_up(row, col):
    def box_cells_above(row, col):
        if grid[row][col] == '#':
            return None

        if grid[row][col] == '.':
            return set()

        cells = {(row, col)}
        children_1 = box_cells_above(row - 1, col)
        children_2 = None
        if grid[row][col] == ']':
            cells.add((row, col - 1))
            children_2 = box_cells_above(row - 1, col - 1)
        elif grid[row][col] == '[':
            cells.add((row, col + 1))
            children_2 = box_cells_above(row - 1, col + 1)

        if children_1 is None or children_2 is None:
            return None

        return cells.union(children_1, children_2)

    cells = box_cells_above(row, col)
    if cells is None:
        return

    for c_row, c_col in sorted(list(cells)):
        grid[c_row - 1][c_col] = grid[c_row][c_col]
        grid[c_row][c_col] = '.'

def move_boxes_down(row, col):
    def box_cells_below(row, col):
        if grid[row][col] == '#':
            return None

        if grid[row][col] == '.':
            return set()

        cells = {(row, col)}
        children_1 = box_cells_below(row + 1, col)
        children_2 = None
        if grid[row][col] == ']':
            cells.add((row, col - 1))
            children_2 = box_cells_below(row + 1, col - 1)
        elif grid[row][col] == '[':
            cells.add((row, col + 1))
            children_2 = box_cells_below(row + 1, col + 1)

        if children_1 is None or children_2 is None:
            return None

        return cells.union(children_1, children_2)

    cells = box_cells_below(row, col)
    if cells is None: return

    for c_row, c_col in sorted(list(cells), reverse=True):
        grid[c_row + 1][c_col] = grid[c_row][c_col]
        grid[c_row][c_col] = '.'

def move_boxes_left(row, col):
    empty_cell_col = col
    while empty_cell_col > 0 and is_box(row, empty_cell_col):
        empty_cell_col -= 1

    if is_obstacle(row, empty_cell_col) or empty_cell_col <= 0:
        return

    while empty_cell_col < col:
        grid[row][empty_cell_col] = grid[row][empty_cell_col + 1]
        grid[row][empty_cell_col + 1] = '.'
        empty_cell_col += 1

def move_boxes_right(row, col):
    empty_cell_col = col
    while empty_cell_col < COLS and is_box(row, empty_cell_col):
        empty_cell_col += 1

    if is_obstacle(row, empty_cell_col) or empty_cell_col >= COLS:
        return

    while empty_cell_col > col:
        grid[row][empty_cell_col] = grid[row][empty_cell_col - 1]
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
    print(get_grid_string())

def box_gps_coord(row, col):
    return (row * 100) + col


row, col = start_row, start_col
for direction in movements:
    row, col = move(row, col, direction)
print_grid()

solution = 0
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == '[':
            solution += box_gps_coord(row, col)

print(solution)