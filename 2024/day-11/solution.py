with open("input.txt") as f:
    data = f.read().strip()

nums = list(map(int, data.split(' ')))

def evolve(num, level, target_level, memo = {}):
    key = f"{num}::{level}"
    if key in memo:
        return memo[key]

    if level == target_level:
        return 1

    num_len = len(str(num))
    if num == 0:
        res = evolve(1, level + 1, target_level, memo)
    elif num_len % 2 == 0:
        mid = num_len // 2
        first_half = int(str(num)[:mid])
        second_half = int(str(num)[mid:])
        res = (evolve(first_half, level + 1, target_level, memo) +
               evolve(second_half, level + 1, target_level, memo))
    else:
        res = evolve(num * 2024, level + 1, target_level, memo)

    memo[key] = res
    return memo[key]

solution1 = sum(evolve(num, 0, 25, {}) for num in nums)
solution2 = sum(evolve(num, 0, 75, {}) for num in nums)
print(solution1)
print(solution2)
