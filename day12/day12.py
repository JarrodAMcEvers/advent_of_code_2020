from functools import reduce

east = 'east'
south = 'south'
west = 'west'
north = 'north'

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

left_rotation = {
    east: north,
    north: west,
    west: south,
    south: east
}
right_rotation = {
    east: south,
    south: west,
    west: north,
    north: east
}
shorthand_map = {
    north: 'N',
    south : 'S',
    east: 'E',
    west: 'W'
}

class Ship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'east'

    def move(self, action, number):
        if action == 'N':
            self.y += number
        elif action == 'S':
            self.y -= number
        elif action == 'E':
            self.x += number
        elif action == 'W':
            self.x -= number
        elif action == 'L':
            rotations = number // 90
            for j in range(rotations):
                self.direction = left_rotation[self.direction]
        elif action == 'R':
            rotations = number // 90
            for j in range(rotations):
                self.direction = right_rotation[self.direction]
        elif action == 'F':
            self.move(shorthand_map[self.direction], number)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


def part1():
    ship = Ship()
    [ ship.move(line[0], int(line[1:])) for line in lines ]
    return ship.manhattan_distance()

print('Part 1:', part1())
