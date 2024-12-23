from collections import deque, defaultdict

with open("input.txt") as f:
    data = f.read().strip()

inputs = data.split("\n")
limit = 16777216
counts = {}
patterns = defaultdict(int)

def simulate(num, iteration):
    secret = num
    prev = num % 10
    changes = deque()
    last_5_digits = deque([prev])
    seen_patterns = set()

    for i in range(iteration):
        secret = ((secret * 64) ^ secret) % limit
        secret = ((secret // 32) ^ secret) % limit
        secret = ((secret * 2048) ^ secret) % limit
        cur = secret % 10
        changes.append(cur - prev)
        last_5_digits.append(cur)

        if len(changes) > 4:
            changes.popleft()

        if len(last_5_digits) > 5:
            last_5_digits.popleft()

        changes_tuple = tuple(changes)
        if i >= 3 and changes_tuple not in seen_patterns:
            seen_patterns.add(changes_tuple)
            patterns[changes_tuple] += sum(changes_tuple) + last_5_digits[0]

        prev = cur

    return secret

solution1 = sum(simulate(int(num), 2000) for num in inputs)
solution2 = max(patterns.values())
print(solution1)
print(solution2)