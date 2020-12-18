
import sys
file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(file, 'r') as f:
    lines = [ str(line) for line in f.read().split('\n') ]

from collections import Counter
from itertools import product

# cell = (x,y,z) or cell = (w,x,y,z)
def get_neighbors(cell: tuple):
    # get all permutations based on length of cell
    # product returns a cartesian product
    neighbors = [ tuple(cell[i] + v[i] for i in range(len(cell))) for v in product([-1, 0, 1], repeat=len(cell)) ]
    # I can't be my own neighbor, now can I?
    neighbors.remove(cell)
    return neighbors

def solve(layout, dimensions):
    extra_dimensions = (0,) * (dimensions - 2)
    active = []
    for x, line in enumerate(layout):
        for y, cell in enumerate(line):
            # add the dimensions of the active cell
            if cell == '#':
                active += [(x,y) + extra_dimensions]

    # iterate 6 times
    # only keep count of the cells that are active
    for j in range(6):
        new_active = []
        # count up all the neighbors for all of the cells
        neighbors = Counter(neighbor for cell in active for neighbor in get_neighbors(cell))

        for cell, neighborCount in neighbors.items():
            if neighborCount == 3 or (cell in active and neighborCount == 2):
                new_active.append(cell)
        active = new_active.copy()

    return len(active)

print("Part 1:", solve(lines, 3))
print("Part 2:", solve(lines, 4))