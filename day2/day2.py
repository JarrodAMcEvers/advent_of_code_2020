import re

with open('./input.txt', 'r') as f:
    lines = [ item for item in f.read().splitlines() ]

def valid_passwords_part1():
    valid_count = 0
    for line in lines:
        tokens = line.split(' ')
        password = tokens[2].replace(' ', '')
        range = [ int(num) for num in tokens[0].split('-') ]
        char_to_find = tokens[1].replace(':', '')
        matches = []
        for char in password:
            if char == char_to_find:
                matches.append(char)
        if len(matches) >= range[0] and len(matches) <= range[1]:
            valid_count += 1

    print(valid_count)

def valid_passwords_part2():
    valid_count = 0
    for line in lines:
        tokens = line.split(' ')
        password = tokens[2].replace(' ', '')
        range = [ int(num) for num in tokens[0].split('-') ]
        char_to_find = tokens[1].replace(':', '')

        first_match = password[range[0] - 1] == char_to_find
        second_match = password[range[1] - 1] == char_to_find
        if first_match ^ second_match:
            valid_count += 1

    print(valid_count)

valid_passwords_part1()
valid_passwords_part2()