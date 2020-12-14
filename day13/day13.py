# pip install numpy
import np
import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

regex = re.compile(r'[0-9]{1,}')
def part1():
    timestamp = int(lines[0])
    buses = [ int(num) for num in regex.findall(lines[1]) ]

    minutes_waited = 0
    while True:
        for bus in buses:
            if timestamp % bus == 0:
                return bus * minutes_waited
        timestamp += 1
        minutes_waited += 1

def part2():
    buses = []
    for index, bus in enumerate(lines[1].split(',')):
        if bus.isdigit():
            buses.append((index, int(bus)))
    first_bus = buses[0][1]

    # set timestamp to first number after timestamp in file that is divisible by the ID of the first bus
    timestamp = int(lines[0])
    for j in range(timestamp, timestamp + first_bus):
        if j % first_bus == 0:
            timestamp = j
            break

    # increment by ID of first bus
    step = first_bus

    for bus in buses:
        while True:
            if (timestamp + bus[0]) % bus[1] == 0:
                break
            # skip to a timestamp where it matches when the first bus will stop or is a common multiple with the previous bus
            timestamp += step
        # find least common multiple between the first and current buses
        step = np.lcm(step, bus[1])
    return timestamp

print('Part 1:', part1())
print('Part 2:', part2())
