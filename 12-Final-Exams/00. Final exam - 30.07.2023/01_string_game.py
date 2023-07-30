def replace_char(text, command):
    action, substring, replacement = command.split()
    text = text.replace(substring, replacement)
    print(text)
    return text


def check_substring(text, command):
    action, substring = command.split()
    if substring in text:
        print(True)
    else:
        print(False)
    return text


def endswith_check(text, command):
    action, substring = command.split()
    if text.endswith(substring):
        print(True)
    else:
        print(False)
    return text


def uppercase_transformation(text):
    text = text.upper()
    print(text)
    return text


def find_index(text, command):
    action, substring = command.split()
    index = text.find(substring)
    print(index)
    return text


def cut_substring(text, command):
    action, start_index, count = command.split()
    substring = text[int(start_index): int(start_index) +7 ]
    text = substring
    print(text)
    return text


string_to_modify = input()
current_command = input()

while current_command != 'Done':
    if current_command.startswith('Change'):
        string_to_modify = replace_char(string_to_modify, current_command)
    elif current_command.startswith('Includes'):
        string_to_modify = check_substring(string_to_modify, current_command)
    elif current_command.startswith('End'):
        string_to_modify = endswith_check(string_to_modify, current_command)
    elif current_command == 'Uppercase':
        string_to_modify = uppercase_transformation(string_to_modify)
    elif current_command.startswith('FindIndex'):
        string_to_modify = find_index(string_to_modify, current_command)
    elif current_command.startswith('Cut'):
        string_to_modify = cut_substring(string_to_modify, current_command)
    current_command = input()

