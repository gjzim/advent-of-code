import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
equations = [list(map(int, re.split("[\s:]+", line))) for line in lines]

def calibrate(nums, operators):
    target, terms = nums[0], nums[1:]

    def can_be_calibrated(pre = 0, i = 0, op = ''):
        if pre > target:
            return False

        if i == len(terms):
            return pre == target

        cur = terms[i]
        if i == 0:
            pre = cur
        elif op == '+':
            pre += cur
        elif op == '*':
            pre *= cur
        elif op == '||':
            pre = int(str(pre) + str(cur))

        for op in operators:
            if can_be_calibrated(pre, i + 1, op):
                return True

        return False

    return target if can_be_calibrated() else 0

solution1 = sum(calibrate(equation, ['+', '*']) for equation in equations)
solution2 = sum(calibrate(equation, ['+', '*', '||']) for equation in equations)

print(solution1)
print(solution2)