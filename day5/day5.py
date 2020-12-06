import math
with open('./input.txt', 'r') as f:
    lines = f.read().splitlines()

def shimmy_down(list, char):
    if char == 'F' or char == 'L':
        return list[:len(list)//2]
    if char == 'B' or char == 'R':
        return list[len(list)//2:]

highest_seat_id = 0
ids = []
for line in lines:
    rows = list(range(128))
    for char in line[:7]:
        rows = shimmy_down(rows, char)
    seats = list(range(8))
    for char in line[7:]:
        seats = shimmy_down(seats, char)

    value = rows[0] * 8 + seats[0]
    ids.append(value)
    if value > highest_seat_id:
        highest_seat_id = value

print('Part 1:', highest_seat_id)

ids.sort()
missing_num = ids[0]
for index in range(1, len(ids)):
    if ids[index] == missing_num + 1:
        missing_num = ids[index]

print('Part 2:', missing_num + 1)