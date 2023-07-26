def insert_space(command, text):
    index = command.split(':|:')[1]
    left_side = text[:int(index)]
    right_side = text[int(index):]
    return left_side + ' ' + right_side


def reverse(command, text):
    substring = command.split(':|:')[1]
    text = text.replace(substring, "", 1)
    return text + substring[::-1]


def replace(command, text):
    substring = command.split(':|:')[1]
    replacement = command.split(':|:')[2]
    if substring in text:
        text = text.replace(substring, replacement)
        return text
    else:
        return text


message = input()
current_command = input()

while current_command != 'Reveal':
    if current_command.startswith('InsertSpace'):
        message = insert_space(current_command, message)
        print(message)
    elif current_command.startswith('Reverse'):
        if current_command[10:] in message:
            message = reverse(current_command, message)
            print(message)
        else:
            print('error')
    elif current_command.startswith('ChangeAll'):
        message = replace(current_command, message)
        print(message)

    current_command = input()

print(f'You have a new text message: {message}')
