import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
nums = [list(map(int, re.split('\s+', line))) for line in lines]
list1, list2 = list(map(itemgetter(0), nums)), list(map(itemgetter(1), nums))

def solution1():
    sl1, sl2 = sorted(list1), sorted(list2)
    return sum([abs(sl1[i] - sl2[i]) for i in range(len(sl1))])

def solution2():
    counts = collections.Counter(list2)
    return sum([num * counts.get(num, 0) for num in list1])

print(solution1())
print(solution2())

