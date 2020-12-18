from operator import mul, add
import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    lines = [ line.strip() for line in f.read().splitlines() ]

operation = {
    '*': mul,
    '+': add
}

def solve_within_parentheses(stack, part2=False):
    new_stack = []
    # go until you get to the first ( of the equation
    while stack[-1] != '(':
        item = stack.pop()
        if part2:
            if item == '+':
                new_stack.append(int(stack.pop()) + int(new_stack.pop()))
            else:
                new_stack.append(item)
        else:
            new_stack.append(item)
    # remove (
    stack.pop()

    # perform operations until there are no more numbers or operators left
    while len(new_stack) > 2:
        num1, op, num2 = int(new_stack.pop()), new_stack.pop(), int(new_stack.pop())
        new_stack.append(operation[op](num1, num2))
    # add new number to stack
    stack.append(new_stack[0])

    return stack

def solve_equation(equation, part2=False):
    stack = []
    equation = '(' + equation.replace(' ', '') + ')'

    # if character is not ), add to stack
    # if character is ), parse
    for char in equation:
        if char != ')':
            stack.append(char)
        else:
            stack = solve_within_parentheses(stack, part2)
    return stack[0]

part1 = sum([solve_equation(equation, False) for equation in lines])
part2 = sum([solve_equation(equation, True) for equation in lines])
print('Part 1:', part1)
print('Part 2:', part2)