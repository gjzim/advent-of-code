import re

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split('\n')

# area = 11, 7
area = 101, 103

def to_robot(line):
    matches = re.search('p=([+\-\d]+),([+\-\d]+)\sv=([+\-\d]+),([+\-\d]+)', line)
    return {
        'p': (int(matches.group(1)), int(matches.group(2))),
        'v': (int(matches.group(3)), int(matches.group(4)))
    }

robots = list(map(to_robot, lines))

def get_robot_position(robot, time):
    start_x, start_y = robot['p']
    velocity_x, velocity_y = robot['v']
    area_x, area_y = area
    x = start_x + (time * velocity_x)
    y = start_y + (time * velocity_y)
    return x % area_x, y % area_y

def get_quadrant(pos):
    x, y = pos
    area_x, area_y = area
    mid_x, mid_y = area_x // 2, area_y // 2

    if x <= mid_x - 1 and y <= mid_y - 1:
        return 0
    elif x >= mid_x + 1 and y <= mid_y - 1:
        return 1
    elif x <= mid_x - 1 and y >= mid_y + 1:
        return 2
    elif x >= mid_x + 1 and y >= mid_y + 1:
        return 3
    else:
        return 4

def get_room(time):
    area_x, area_y = area
    room = [['.' for _ in range(area_x)] for _ in range(area_y)]
    for robot in robots:
        x, y = get_robot_position(robot, time)
        if room[y][x] == '*':
            return None

        room[y][x] = '*'

    return room

def print_room(room, time):
    area_x, area_y = area
    output = f"{'-' * (area_x // 2)}{time}s{'-' * (area_x // 2)}\n"
    for line in room:
        for cell in line:
            output += cell
        output += '\n'
    output += '-' * area_x + '\n\n\n'
    print(output)

quads = [0] * 5
for robot in robots:
    quads[get_quadrant(get_robot_position(robot, 100))] += 1

solution1 = quads[0] * quads[1] * quads[2] * quads[3]

solution2 = 0
while True:
    solution2 += 1
    room = get_room(solution2)
    if room is None:
        continue

    # print_room(room, solution2)
    break

print(solution1)
print(solution2)