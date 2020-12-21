from collections import defaultdict
import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    lines = [ line.strip() for line in f.read().split('\n') ]

### Part 1
all_allergens = set()
all_ingredients = set()
count = defaultdict(int)
for line in lines:
    ingredients, allergens = line.split('(contains ')
    ingredients = set(ingredients.split())
    for ingredient in ingredients:
        count[ingredient] += 1
    allergens = set(allergens[:-1].split(', '))

    # extend existing sets
    all_ingredients |= ingredients
    all_allergens |= allergens

# with the ingredient as the key, we will track what allergens the ingredient does not contain
not_allergens = {ingredient: set() for ingredient in all_ingredients}
for line in lines:
    ingredients, allergens = line.split('(contains ')
    ingredients = set(ingredients.split())
    allergens = set(allergens[:-1].split(', '))

    for allergen in allergens:
        for ingredient in all_ingredients:
            if ingredient not in ingredients:
                not_allergens[ingredient].add(allergen)
part1 = sum([count[j] for j in not_allergens if not_allergens[j] == all_allergens])
print('Part 1:', part1)

### Part 2
solved_dict = {}
for j in not_allergens:
    remaining = all_allergens - not_allergens[j] - set(solved_dict)
    if len(remaining):
        allergen = ','.join(remaining)
        solved_dict[j] = allergen


solved = [ v for k,v in solved_dict.items() if len(solved_dict[k].split(',')) == 1 ]
while len(solved) != len(all_allergens):
    for k,v in solved_dict.items():
        if v in solved:
            continue
        else:
            new_set = set(v.split(',')) - set(solved)
            if len(new_set) == 1:
                solved_dict[k] = ''.join(list(new_set))
                solved.append(''.join(list(new_set)))

part2 = ",".join(j[0] for j in sorted(solved_dict.items(), key=lambda item: item[1]))
print('Part 2:', part2)
