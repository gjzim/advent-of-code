import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
reports = [list(map(int, re.split('\s', line))) for line in lines]

def is_monotonic(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

def is_in_range(arr, low = 1, high = 3):
    return all( low <= abs(arr[i + 1] - arr[i]) <= high for i in range(len(arr) - 1))

def is_safe(report, with_variation):
    variations = [report]
    if with_variation:
        variations += [report[:i] + report[i+1:] for i in range(len(report))]

    return any(is_monotonic(variation) and is_in_range(variation) for variation in variations)

solution1 = sum([is_safe(report, False) for report in reports])
solution2 = sum([is_safe(report, True) for report in reports])

print(solution1)
print(solution2)

