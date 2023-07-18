number_of_letters = int(input())

start_letter_index = 97

for first_letter_index in range(start_letter_index, start_letter_index+number_of_letters):
    for second_letter_index in range(start_letter_index, start_letter_index + number_of_letters):
        for third_letter_index in range(start_letter_index, start_letter_index + number_of_letters):
            output = chr(first_letter_index)+chr(second_letter_index)+chr(third_letter_index)
            print(output)
