sequence_of_integers = input().split()
max_index = None
value_to_use = None
removed = []

while sequence_of_integers:
    current_index = int(input())
    max_index = len(sequence_of_integers) - 1
    sequence_of_integers = [int(el) for el in sequence_of_integers]

    if current_index < 0:
        value_to_use = int(sequence_of_integers[0])
        removed.append(sequence_of_integers[0])
        sequence_of_integers[0], sequence_of_integers[-1] = sequence_of_integers[-1], sequence_of_integers[-1]
    elif current_index > max_index:
        value_to_use = int(sequence_of_integers[-1])
        removed.append(sequence_of_integers[-1])
        sequence_of_integers[0], sequence_of_integers[-1] = sequence_of_integers[0], sequence_of_integers[0]
    else:
        value_to_use = int(sequence_of_integers[current_index])
        removed.append(sequence_of_integers[current_index])
        sequence_of_integers.pop(current_index)

    for ind, el in enumerate(sequence_of_integers):
        if el <= value_to_use:
            el += value_to_use
            sequence_of_integers[ind] = el
        elif el > value_to_use:
            el -= value_to_use
            sequence_of_integers[ind] = el

    max_index -= 1
print(sum(removed))

    
