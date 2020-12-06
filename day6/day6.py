with open('./input.txt', 'r') as f:
    lines = f.read().split('\n\n')

def sort(a, b):
    if len(a) < len(b):
        return 1
    elif len(a) == len(b):
        return 0

    return -1

def part1():
    total = sum([ len(set(line.replace('\n', ''))) for line in lines ])
    print('part1:', total)

def part2():
    sum = 0
    for line in lines:
        sorted_line = sorted(line.split('\n'), key=lambda a: len(a))
        if len(sorted_line) == 1:
            sum += len(sorted_line[0])
            continue

        for char in sorted_line[0]:
            answered = []
            for index in range(1, len(sorted_line)):
                if char in sorted_line[index]:
                    if index == len(sorted_line) - 1:
                        answered.append(char)
                    continue
                else:
                    break

            sum += len(answered)
    print('part2:', sum)

part1()
part2()