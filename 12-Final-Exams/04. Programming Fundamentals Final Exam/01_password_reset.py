def take_odd(text):
    output = ''
    for index in range(len(text)):
        if index % 2 != 0:
            output += text[index]
    return output


def cut_text(text, command):
    action, index, length = command.split()
    substring = text[int(index):int(index) + int(length)]
    output = text.replace(substring, "", 1)
    return output


def substitute_text(text, command):
    action, substring, substitute = command.split()
    if substring in text:
        output = text.replace(substring, substitute)
        return output
    else:
        print('Nothing to replace!')
        return text


password = input()
current_command = input()

while current_command != 'Done':
    if current_command == 'TakeOdd':
        # output = ''
        # for index in range(len(password)):
        #     if index % 2 != 0:
        #         output += password[index]
        # password = output
        password = take_odd(password)
        print(password)
    elif current_command.startswith('Cut'):
        # action, index, length = current_command.split()
        # substring = password[int(index):int(index) + int(length)]
        # output = password.replace(substring, "", 1)
        # password = output
        password = cut_text(password, current_command)
        print(password)
    elif current_command.startswith('Substitute'):
        function_output = substitute_text(password, current_command)
        if current_command.split()[1] in password:
            password = function_output
            print(function_output)

    current_command = input()
print(f'Your password is: {password}')
