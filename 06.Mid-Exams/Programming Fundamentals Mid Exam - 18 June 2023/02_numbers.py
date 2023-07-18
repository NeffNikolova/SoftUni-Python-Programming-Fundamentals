sequence_numbers = input().split()
sequence_numbers = [int(el) for el in sequence_numbers]
command = input()

while command != 'Finish':
    if 'Add' in command:
        action, value = command.split()
        value = int(value)
        sequence_numbers.append(value)
    elif 'Remove' in command:
        action, value = command.split()
        value = int(value)
        if value in sequence_numbers:
            sequence_numbers.remove(value)
    elif 'Replace' in command:
        action, value, replacement = command.split()
        value = int(value)
        replacement = int(replacement)
        if value in sequence_numbers:
            sequence_numbers[sequence_numbers.index(value)] = replacement
    elif 'Collapse' in command:
        action, value = command.split()
        value = int(value)
        sequence_numbers = [el for el in sequence_numbers if el>= value]
    command = input()
else:
    print(*sequence_numbers, sep=' ')

