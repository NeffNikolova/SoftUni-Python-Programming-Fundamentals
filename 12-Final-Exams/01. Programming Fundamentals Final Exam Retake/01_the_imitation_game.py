def move_characters(original_message, number_of_letters):
    addition = original_message[:number_of_letters]
    result = original_message[number_of_letters:] + addition
    return result


def insert_value(original_message, index:int, value):
    left_part = original_message[:index]
    right_part = original_message[index:]
    result = left_part + value + right_part
    return result


def replace_characters(original_message, old_value, new_value):
    result = original_message.replace(old_value, new_value)
    return result


message = input()
command = input()
while command != 'Decode':
    action = command.split('|')[0]
    if action == 'Move':
        message = move_characters(message, int(command.split('|')[1]))
    elif action == 'Insert':
        message = insert_value(message, int(command.split('|')[1]), command.split('|')[2])
    elif action == 'ChangeAll':
        message = replace_characters(message, command.split('|')[1], command.split('|')[2])
    command = input()
print(f'The decrypted message is: {message}')

