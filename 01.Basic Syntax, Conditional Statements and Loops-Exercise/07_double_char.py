current_string = input()

character = ''
final_string = ''
while current_string != 'End':
    if current_string != 'SoftUni':
        for i in range(len(current_string)):
            character = current_string[i]
            final_string += character * 2
        print(final_string)
        final_string = ''
    current_string = input()

