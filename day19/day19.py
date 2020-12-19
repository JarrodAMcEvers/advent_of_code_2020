import re

import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    rules, lines = [ line.strip() for line in f.read().split('\n\n') ]

MAX_DEPTH = 5
lines = lines.split('\n')
rules = { int(rule.split(':')[0]): rule.split(':')[1].strip() for rule in rules.split('\n') }
solved = {}

def solve_part1(rule_number) -> str:
    rule_number = int(rule_number)
    item = rules[rule_number]
    temp = '('
    if '"' in item:
        return item.replace('"', '')
    else:
        if '|' in item:
            nums1, nums2 = item.split('|')
            nums1 = nums1.strip()
            nums2 = nums2.strip()
            for num in nums1.split(' '):
                temp += solve_part1(num)
            temp += '|'
            for num in nums2.split(' '):
                temp += solve_part1(num)
            return temp + ')'
        else:
            for number in item.split(' '):
                temp += solve_part1(number)
            return temp + ')'
def part1():
    solved[0] = solve_part1(0)
    regex = '^{}$'.format(solved[0])
    return len(list(filter(lambda x: re.match(regex, x), lines)))

print('Part 1:', part1())
