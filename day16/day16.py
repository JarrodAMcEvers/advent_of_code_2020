import re

with open('input.txt', 'r') as f:
    lines = f.read()

sections = lines.split('\n\n')
my_ticket = [ int(number) for number in sections[1].split('\n')[1].split(',') ]
ranges = []

def part1():
    ticket_rules_regex = re.compile(r'(.*): (\d{1,})-(\d{1,}) or (\d{1,})-(\d{1,})$')

    numbers = set()
    for line in sections[0].split('\n'):
        matches = re.findall(ticket_rules_regex, line)
        for match in matches:
            name, lower1, upper1, lower2, upper2 = match
            ranges.append({ 'name': name, 'lower': int(lower1), 'upper': int(upper1), 'lower1': int(lower2), 'upper1': int(upper2) })
            for j in range(int(lower1), int(upper1)+1):
                numbers.add(j)
            for j in range(int(lower2), int(upper2)+1):
                numbers.add(j)
    numbers = list(numbers)

    invalid = []
    nearby_tickets = sections[2].split('\n')[1:]
    for index, ticket in enumerate(nearby_tickets):
        for num in ticket.split(','):
            num = int(num)
            if num not in numbers:
                invalid.append(num)
                nearby_tickets[index] = None
                break

    # filter out None items
    return sum(invalid), [ ticket for ticket in nearby_tickets if ticket is not None]

def part2(tickets):
    unfit = []
    for ticket in tickets:
        ticket = ticket.split(',')
        for index, item in enumerate(ticket):
            value = int(item)
            for rng in ranges:
                # put name of field and index of ticket where the value is invalid
                if (rng['lower'] > value or value > rng['upper']) and (rng['lower1'] > value or value > rng['upper1']):
                    unfit.append([rng['name'], index])
    set_names = set([ v['name'] for v in ranges])

    ticket_spec = {}
    def check(set_of_names):
        for column in range(len(tickets[0].split(','))):
            # find all fields that are invalid for the column of the ticket
            filtered = set([ item[0] for item in unfit if item[1] == column ])
            # subtract the invalid fields from all the fields
            left_over = set_names - filtered
            # if there is one field left, we have figured out the mystery column
            if len(left_over) == 1:
                name_from_set = left_over.pop()
                ticket_spec[column] = name_from_set
                set_of_names.remove(name_from_set)
        return set_names

    # continue to run until all the fields have been figured out
    # as fields get identified we will want to check all the tickets again to see if we can figure out any new fields
    while len(set_names) > 0:
        set_names = check(set_names)

    departure_indices = [ key for key in ticket_spec if 'departure' in ticket_spec[key] ]
    total = 1
    for k in departure_indices:
        total *= my_ticket[k]
    return total

part1_total, valid_tickets = part1()
print('Part 1:', part1_total)
print('Part 2:', part2(valid_tickets))