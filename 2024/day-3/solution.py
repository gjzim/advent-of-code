import re
import collections
from operator import itemgetter

with open("input.txt") as f:
    data = f.read().strip()

def evaluate(memory, conditional):
    expressions = re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', memory)
    do, res = True, 0
    for exp in expressions:
        exp = [token for token in exp if token]
        if len(exp) == 1:
            do = not conditional or exp[0] == 'do()'
        elif do:
            l, r = exp
            res += (int(l) * int(r))
    return res

solution1 = evaluate(data, False)
solution2 = evaluate(data, True)

print(solution1)
print(solution2)