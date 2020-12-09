import itertools

with open('input.txt', 'r') as f:
    lines = [ int(item) for item in f.read().splitlines() ]

def part1():
    index = 26
    while index <= len(lines) - 1:
        combinations = [sum(combo) for combo in itertools.combinations(lines[index-25:index], 2)]
        if lines[index] not in combinations:
            return index, lines[index]
        index += 1


def part2(index, target):
    for i in range(len(lines[:index])):
        index = i
        sum = 0
        while sum < target:
            sum += lines[index]
            index += 1
        if sum == target:
            range_set = lines[i:index]
            return min(range_set) + max(range_set)

index_of_answer, answer = part1()
print('Part 1:', answer)
print('Part 2:', part2(index_of_answer, answer))