magic_number = 2020
f = open('./input.txt', 'r')
lines = [ int(item) for item in f.read().splitlines() ]
f.close()

def multiply_two_values_that_add_to_2020():
    for index1, line in enumerate(lines):
        for index2 in range(1, len(lines)):
            if index2 == index1:
                continue
            if (lines[index1] + lines[index2]) == magic_number:
                return lines[index1] * lines[index2]

def multiply_three_values_that_add_to_2020():
    length = len(lines)
    for j, number in enumerate(lines):
        for index1 in range(1, length):
            for index2 in range(2, length):
                if j == index1 or j == index2 or index1 == index2:
                    continue
                if (lines[j] + lines[index1] + lines[index2]) == magic_number:
                    return lines[j] * lines[index2] * lines[index1]

print(multiply_two_values_that_add_to_2020())
print(multiply_three_values_that_add_to_2020())
