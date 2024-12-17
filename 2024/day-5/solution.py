import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

sections = data.split("\n\n")
ordering_rules = [list(map(int, line.split('|'))) for line in sections[0].split("\n")]
updates = [list(map(int, line.split(','))) for line in sections[1].split("\n")]

orders_for_page = collections.defaultdict(set)
for before, after in ordering_rules:
    orders_for_page[before].add(after)

def is_correctly_ordered(pages):
    pages = pages[::-1]
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[j] in orders_for_page[pages[i]]:
                return False

    return True

def order_pages_correctly(pages):
    i = 0
    while not is_correctly_ordered(pages):
        while i < len(pages):
            j = i + 1
            while j < len(pages):
                if pages[j] not in orders_for_page[pages[i]]:
                    pages[i], pages[j] = pages[j], pages[i]
                    i = 0
                else:
                    j += 1
            i += 1

    return pages

solution1 = solution2 = 0
for pages in updates:
    if is_correctly_ordered(pages):
        solution1 += pages[len(pages) // 2]
    else:
        pages = order_pages_correctly(pages)
        solution2 += pages[len(pages) // 2]

print(solution1)
print(solution2)