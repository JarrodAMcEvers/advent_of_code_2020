with open('./input.txt', 'r') as f:
    lines = f.read().splitlines()

def part1(lines):
    instruction_list = []
    index = 0
    accumulator = 0
    while index not in instruction_list:
        instruction_list.append(index)
        command, num = lines[index].split(' ')
        num = int(num)
        if command == 'nop':
            index += 1
        elif command == 'acc':
            accumulator += num
            index += 1
        elif command == 'jmp':
            index += num

    return accumulator

map = {
    'jmp': 'nop',
    'nop': 'jmp'
}
def run_part2(instructions):
    instruction_list = []
    index = 0
    accumulator = 0
    while index not in instruction_list and index < len(instructions):
        instruction_list.append(index)
        command, num = instructions[index].split(' ')
        num = int(num)
        if command == 'nop':
            index += 1
        elif command == 'acc':
            accumulator += num
            index += 1
        elif command == 'jmp':
            index += num

    if index >= len(instructions):
        return accumulator

    return None


def part2(lines):
    for index, line in enumerate(lines):
        command, num = lines[index].split(' ')
        if command == 'acc':
            continue
        lines_copy = lines.copy()
        lines_copy[index] = '{} {}'.format(map[command], num)
        answer = run_part2(lines_copy)

        if answer:
            return answer


print('Part 1:', part1(lines))
print('Part 2:', part2(lines))