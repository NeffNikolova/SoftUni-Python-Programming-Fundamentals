original_message = input().split()
first_letter = []
rest_of_element = []

for element in original_message:
    first_letter = [letter for letter in element if letter.isnumeric()]
    rest_of_element = [letter for letter in element if letter not in first_letter]
    rest_of_element[0], rest_of_element[-1] = rest_of_element[-1], rest_of_element[0]

    print((chr(int(''.join(first_letter)))), end='')
    print(*rest_of_element, sep='', end=' ')

