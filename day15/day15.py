from collections import defaultdict

with open('input.txt', 'r') as f:
    numbers = [ int(number) for number in f.read().split(',') ]

def solve(iterations):
    arr = numbers.copy()
    arr += [None] * (iterations - len(numbers))
    # dictionary of the turns a number was spoken
    # use defaultdict to set any keys that don't exist to an empty list
    # this makes it so I don't have to do an existence check
    dict = defaultdict(list)
    for index, number in enumerate(numbers):
        dict[number] = [index + 1]
    # dict = {v:[k+1] for k, v in enumerate(numbers) }

    j = len(numbers)
    while True:
        if j == iterations:
            break
        last_index = j - 1
        number = arr[last_index]
        item = dict.get(number, None)
        turn = j + 1

        if not item:
            # first time the number has been spoken
            arr[j] = number
            dict[number] = [turn]
        else:
            # if number has been spoken only once, add turn to list and set number to 0
            if len(item) == 1:
                dict[0].extend([turn])
                arr[j] = 0
            elif len(item) > 1:
                # subtract 2nd most recent turn from most recent turn for the next number
                next_number = item[-1] - item[-2]
                dict[next_number].extend([turn])
                arr[j] = next_number
        j += 1
    return arr[iterations - 1]

print('Part 1:', solve(2020))
print('Part 2:', solve(30000000))