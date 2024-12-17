import re

with open("input.txt") as f:
    data = f.read().strip()

registers, program = data.split('\n\n')
registers = {
    'a': int(re.search('Register A: (\d+)', registers).group(1)),
    'b': int(re.search('Register B: (\d+)', registers).group(1)),
    'c': int(re.search('Register C: (\d+)', registers).group(1))
}
instructions = list(map(int, re.search('Program: (.*)', program).group(1).split(',')))
output = []
ip = 0

def combo_to_literal(combo):
    if combo <= 3:
        return combo
    elif combo == 4:
        return registers['a']
    elif combo == 5:
        return registers['b']
    elif combo == 6:
        return registers['c']

    return None

def div(operand, reg):
    numerator = registers['a']
    denominator = 2 ** combo_to_literal(operand)
    registers[reg] = numerator // denominator
    return ip + 2

def adv(operand):
    return div(operand, 'a')

def bdv(operand):
    return div(operand, 'b')

def cdv(operand):
    return div(operand, 'c')

def bxl(operand):
    registers['b'] ^= operand
    return ip + 2

def bst(operand):
    registers['b'] = combo_to_literal(operand) % 8
    return ip + 2

def jnz(operand):
    return ip + 2 if registers['a'] == 0 else operand

def bxc(_operand):
    registers['b'] ^= registers['c']
    return ip + 2

def out(operand):
    operand = combo_to_literal(operand)
    output.append(str(operand % 8))
    return ip + 2

operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def operate(opcode, operand):
    op = operations[opcode]
    return op(operand)

while ip < len(instructions):
    ip = operate(
        instructions[ip],
        instructions[ip + 1]
    )

solution1 = ','.join(output)
print(solution1)

def is_valid(a, target):
    b = a % 8
    b ^= 5
    c = a // (2 ** b)
    b ^= 6
    b ^= c

    return b % 8 == target

def dfs(prefix, index):
    if index < 0:
        return [prefix]

    results = []
    for incr in range(8):
        reg_a = (prefix * 8) + incr
        if is_valid(reg_a, instructions[index]):
            results.extend(dfs(reg_a, index - 1))

    return results

solution2 = sorted(dfs(0, len(instructions) - 1))[0]
print(solution2)
