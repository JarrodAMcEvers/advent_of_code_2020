import re

with open('./input.txt', 'r') as f:
    lines = f.read().splitlines()

# set up for part 2
dict = {}
for line in lines:
    r1 = re.compile(r'(.*?) bags')
    r2 = re.compile(r'(?:(\d+)|no other) (.*?) bags*')
    outer_bag = re.match(r1, line).group(1)
    bags = re.findall(r2, line)
    dict[outer_bag] = bags

def part1(color):
    found = []
    for line in lines:
        index = line.find(' bags contain')
        if color in line[index:]:
            found.append(line[:index])
            found.extend(part1(line[:index]))
    return found

def part2(bag_color):
    count = 1
    for name, items in dict.items():
        if bag_color in name:
            for bag_count, color in items:
                count += int(bag_count) * part2(color)
    return count


print('Part 1:', len(set(part1('shiny gold'))))
print('Part 2:', part2('shiny gold') - 1)
