from collections import Counter, defaultdict

with open('input.txt', 'r') as f:
    lines = [ int(item) for item in f.read().splitlines() ]


lines = [0] + sorted(lines)
highest_rating = lines[-1] + 3
lines.append(highest_rating)

def part1():
    counter = Counter(j - i for i, j in zip(lines, lines[1:]))
    return counter[1] * counter[3]

def part2():
    # if key does not exist when trying to reference it, it will auto populate it with int 0.
    dict = defaultdict(int)
    # set starting value to 1 for counting
    dict[lines[-1]] = 1
    del lines[-1]

    # cumulatively add all the previous values to the 0th index
    # start with device's adapter and go down the list to the seat's charging outlet
    for item in reversed(lines):
        dict[item] = dict[item + 1] + dict[item + 2] + dict[item + 3]

    return dict[0]

print('Part 1:', part1())
print('Part 2:', part2())