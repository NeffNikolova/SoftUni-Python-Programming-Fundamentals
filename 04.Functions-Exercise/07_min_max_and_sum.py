def list_of_integers(some_list: list) -> list:
    numbers_list = []
    for item in some_list:
        numbers_list.append(int(item))
    return numbers_list


sequence_of_numbers = input().split()
print(f'The minimum number is {min(list_of_integers(sequence_of_numbers))}')
print(f'The maximum number is {max(list_of_integers(sequence_of_numbers))}')
print(f'The sum number is: {sum(list_of_integers(sequence_of_numbers))}')
