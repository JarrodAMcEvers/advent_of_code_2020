from functools import reduce

with open('./input.txt') as f:
    lines = f.read().splitlines()

def multiply(a, b):
    return a * b

def findTrees(rise, run):
    row = 0
    x = 0
    count = 0
    while row < len(lines):
        current_row = lines[row]
        if current_row[x % len(current_row)] == '#':
            count += 1
        row += rise
        x += run

    return count


total = [findTrees(1, 1), findTrees(1, 3), findTrees(1, 5), findTrees(1, 7), findTrees(2, 1)]
print(reduce(multiply, total))