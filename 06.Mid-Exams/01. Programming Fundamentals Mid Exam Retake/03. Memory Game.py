def add_elements(sequence, moves_):
    mid_index = int((len(sequence)/2))
    new_element = '-' + str(moves_) + 'a'
    sequence.insert(mid_index, new_element)
    sequence.insert(mid_index, new_element)
    return sequence


def remove_elements(sequence, index1, index2):
    if index1 < index2:
        sequence.pop(index2)
        sequence.pop(index1)
    else:
        sequence.pop(index1)
        sequence.pop(index2)
    return sequence


sequence_of_elements = input().split()
command = input()
moves = 0
won = False

while command != 'end':
    moves += 1
    first_index, second_index = command.split()
    max_index = len(sequence_of_elements) - 1
    first_index = int(first_index)
    second_index = int(second_index)

    if (0 > first_index) or (first_index > max_index) or (0 > second_index) or (second_index > max_index) or (first_index == second_index):
        sequence_of_elements = add_elements(sequence_of_elements, moves)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
            sequence_of_elements = remove_elements(sequence_of_elements, first_index, second_index)

        elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
            print("Try again!")

    if not sequence_of_elements:
        print(f"You have won in {moves} turns!")
        break

    command = input()
else:
    print("Sorry you lose :(")
    print(*sequence_of_elements, sep=' ')
