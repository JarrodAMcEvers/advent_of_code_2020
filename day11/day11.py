import re
from copy import deepcopy

regex = re.compile(r'\#')

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def update_seating(input):
    new_lines = input.copy()
    changes = 0
    number_of_rows = len(input) - 1
    for index, line in enumerate(new_lines):
        # convert line to list, you can't update a string using an index
        new_line = list(line)
        for pos, char in enumerate(new_line):
            if index == 0:
                rows_to_check = [index, index + 1]
            elif index == number_of_rows:
                rows_to_check = [index, index - 1]
            else:
                rows_to_check = [index, index + 1, index - 1]

            if pos == 0:
                seats_to_check = [pos, pos + 1]
            elif pos == len(new_line) - 1:
                seats_to_check = [pos, pos - 1]
            else:
                seats_to_check = [pos, pos - 1, pos + 1]

            neighbors = 0
            for row in rows_to_check:
                for seat in seats_to_check:
                    if row == index and seat == pos:
                        continue
                    if input[row][seat] == '#':
                        neighbors += 1

            # Good, no one is around. This is now my seat.
            if neighbors == 0 and char == 'L':
                changes += 1
                new_line[pos] = '#'
            # More than 4 neighbors means I will look for a new seat.
            elif neighbors >= 4 and char == '#':
                changes += 1
                new_line[pos] = 'L'
        # convert the list back to a string for the next iteration
        new_lines[index] = ''.join(new_line)

    return changes, new_lines

def part1():
    adjustments, updated_seating = update_seating(lines)
    while adjustments > 0:
        adjustments, updated_seating = update_seating(updated_seating)
    return sum([ len(regex.findall(line)) for line in updated_seating ])

def part2():
    with open('input.txt', 'r') as f:
        lines = [list(line.strip()) for line in f.read().splitlines()]
    num_rows = len(lines)
    cols = len(lines[0])
    while True:
        newL = deepcopy(lines)
        change = False
        for r in range(num_rows):
            for c in range(cols):
                neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if not (dr == 0 and dc == 0):
                            rr = r + dr
                            cc = c + dc
                            while 0<=rr<num_rows and 0<=cc<cols and lines[rr][cc] == '.':
                                rr = rr + dr
                                cc = cc + dc
                            if 0<=rr<num_rows and 0<=cc<cols and lines[rr][cc] == '#':
                                # print('neighbors!')
                                neighbors += 1
                if lines[r][c] == 'L' and neighbors == 0:
                    newL[r][c] = '#'
                    change = True
                elif lines[r][c] == '#' and neighbors >= 5:
                    newL[r][c] = 'L'
                    change = True
        # break if no changes were found
        if not change:
            break
        lines = deepcopy(newL)
    return sum([ len(regex.findall(''.join(line))) for line in lines ])

print('Part 1: ', part1())
print('Part 2: ', part2())
