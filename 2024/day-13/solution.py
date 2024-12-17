import re
from sympy import symbols, Eq, solve

with open("input.txt") as f:
    data = f.read().strip()

def to_machine(data):
    button_a = re.search('Button A: X\+(\d+), Y\+(\d+)', data)
    button_b = re.search('Button B: X\+(\d+), Y\+(\d+)', data)
    prize = re.search('Prize: X=(\d+), Y=(\d+)', data)

    return {
        'a': {
            'x': int(button_a.group(1)),
            'y': int(button_a.group(2))
        },
        'b': {
            'x': int(button_b.group(1)),
            'y': int(button_b.group(2))
        },
        'p': {
            'x': int(prize.group(1)),
            'y': int(prize.group(2))
        }
    }

machines = list(map(to_machine, data.split("\n\n")))

def solve_soe(machine, add_large_num = False):
    # Define variables
    a, b = symbols('a b')

    # Define equations
    eq1 = Eq(
        machine['a']['x'] * a + machine['b']['x'] * b,
        machine['p']['x'] + 10000000000000 if add_large_num else machine['p']['x']
    )
    eq2 = Eq(
        machine['a']['y'] * a + machine['b']['y'] * b,
        machine['p']['y'] + 10000000000000 if add_large_num else machine['p']['y']
    )

    # Solve equations
    solution = solve((eq1, eq2), (a, b))
    a_value = solution[a]
    b_value = solution[b]

    if a_value.is_integer and b_value.is_integer:
        return (a_value * 3) + (b_value * 1)
    else:
        return 0

solution1 = 0
solution2 = 0
for machine in machines:
    solution1 += solve_soe(machine)
    solution2 += solve_soe(machine, True)

print(solution1)
print(solution2)