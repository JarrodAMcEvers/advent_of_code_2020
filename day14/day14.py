import re
from itertools import product

mem_address_regex = re.compile(r'\[(\d*)\]')
x_regex = re.compile(r'X')
lines = open('input.txt', 'r').read()

def part1() -> int:
    memory = {}
    for line in lines.split('\n'):
        if 'mask' in line:
            mask = line.split(' = ')[1]
            continue
        else:
            memory_address = mem_address_regex.findall(line)[0]
            # get binary string and convert it to a list. this makes it easier to change the bits.
            binary = list(f'{int(line.split(" = ")[1]):036b}')

        for bit in range(len(mask)):
            if mask[bit] == 'X' or mask[bit] == binary[bit]: continue
            binary[bit] = mask[bit]
        # convert binary back to string to store number into memory
        binary = ''.join(binary)
        memory[memory_address] = int(binary, 2)

    return sum(memory.values())

def part2():
    memory = {}
    for line in lines.split('\n'):
        if 'mask' in line:
            mask = line.split(' = ')[1]
            continue
        else:
            memory_address = list(f'{int(mem_address_regex.findall(line)[0]):036b}')
            value = int(line.split(' = ')[1])

        # find indices where X is in the mask
        Xs = []
        for bit in range(len(mask)):
            if mask[bit] == '0': continue
            elif mask[bit] == '1':
                memory_address[bit] = '1'
            elif mask[bit] == 'X':
                Xs.append(bit)
                memory_address[bit] = 'X'

        # find cartesian product of floating values for the number of Xs in the mask
        addresses = []
        for prod in product((0,1), repeat=len(Xs)):
            copy = memory_address.copy()
            prod = list(prod)
            for x in Xs:
                copy[x] = str(prod[0])
                del prod[0]
            addresses.append(copy)

        # convert the list binary into a string then into a decimal
        for address in [ int("".join(addr), 2) for addr in addresses ]:
            memory[address] = value

    return sum(memory.values())

print('Part 1:', part1())
print('Part 2:', part2())

