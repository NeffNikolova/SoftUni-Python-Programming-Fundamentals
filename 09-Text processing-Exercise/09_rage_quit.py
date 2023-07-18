input_string = input()
current_string = ''
current_number = ''
output = ''

for index in range(len(input_string)):
    if not input_string[index].isdigit():
        current_string += input_string[index].capitalize()
    else:
        for index2 in range(index, len(input_string)):
            if input_string[index2].isdigit():
                current_number += input_string[index2]
            elif not input_string[index2].isdigit():
                break
        output += current_string * int(current_number)
        current_string = ''
        current_number = ''

unique_symbols = ''
for character in output:
    if character not in unique_symbols:
        unique_symbols += character

print(f'Unique symbols used: {len(unique_symbols)}\n{output}')