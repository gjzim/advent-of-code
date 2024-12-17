import re
import collections
from collections import defaultdict
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [list(line) for line in lines]
ROWS, COLS = len(grid), len(grid[0])

def out_of_bounds(row, col):
    return row < 0 or row >= ROWS or col < 0 or col >= COLS

def get_anti_node(src, dest, multiplier):
    if src == dest:
        return None

    row = src[0] + (src[0] - dest[0]) * multiplier
    col = src[1] + (src[1] - dest[1]) * multiplier

    return None if out_of_bounds(row, col) else (row, col)

def get_anti_nodes(src, dest):
    anti_nodes = set()
    multiplier = 0
    while get_anti_node(src, dest, multiplier):
        if get_anti_node(src, dest, multiplier):
            anti_nodes.add(get_anti_node(src, dest, multiplier))
        multiplier += 1
    return anti_nodes

antennas_map = defaultdict(set)
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == '.':
            continue

        antennas_map[grid[row][col]].add((row, col))

basic_anti_nodes = set()
for antennas in antennas_map.values():
    for src in antennas:
        for dest in antennas:
            anti_node = get_anti_node(src, dest, 1)
            if anti_node and anti_node not in antennas:
                basic_anti_nodes.add(anti_node)

enhanced_anti_nodes = set()
for antennas in antennas_map.values():
    for src in antennas:
        for dest in antennas:
            enhanced_anti_nodes = enhanced_anti_nodes.union(get_anti_nodes(src, dest))

solution1 = len(basic_anti_nodes)
solution2 = len(enhanced_anti_nodes)
print(solution1)
print(solution2)