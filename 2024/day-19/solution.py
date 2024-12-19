with open("input.txt") as f:
    data = f.read().strip()

sections = data.split('\n\n')
stripes = set(sections[0].split(', '))
targets = sections[1].split('\n')
memo = {}

def solve(index, start):
    key = f"{index},{start}"

    if key in memo:
        return memo[key]

    target = targets[index]
    if start == len(target):
        return 1

    result = 0
    for end in range(start + 1, len(target) + 1):
        cur = target[start:end]
        if cur in stripes:
            result += solve(index, end)

    memo[key] = result
    return memo[key]

solution1 = sum([solve(i, 0) > 0 for i in range(len(targets))])
solution2 = sum([solve(i, 0) for i in range(len(targets))])
print(solution1, solution2)