import re

import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    rules, lines = [ line.strip() for line in f.read().split('\n\n') ]

MAX_DEPTH = 6
lines = lines.split('\n')
rules = { int(rule.split(':')[0]): rule.split(':')[1].strip() for rule in rules.split('\n') }
solved = {}

def solve(rule_number, depth=0) -> str:
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
                temp += solve(num)
            temp += '|'
            for num in nums2.split(' '):
                temp += solve(num)
            return temp + ')'
        else:
            for number in item.split(' '):
                temp += solve(number)
            return temp + ')'
solved[0] = solve(0)

regex = '^' + solved[0] + '$'
part1 = len([1 for item in filter(lambda x: re.match(regex, x), lines)])
print('Part 1:', part1)
