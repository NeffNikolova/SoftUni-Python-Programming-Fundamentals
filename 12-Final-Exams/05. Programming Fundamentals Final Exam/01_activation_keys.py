def contain_substring_check(key, command):
    action, substring = command.split('>>>')
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print("Substring not found!")
    return key


def flip_case(key, command):
    action, case, start_index, end_index = command.split('>>>')
    left_side = key[:int(start_index)]
    right_side = key[int(end_index):]
    substring = key[int(start_index):int(end_index)]
    if case == 'Lower':
        key = left_side + substring.lower() + right_side
    else:
        key = left_side + substring.upper() + right_side
    return key


def slice_key(key, command):
    action, start_index, end_index = command.split('>>>')
    left_side = key[:int(start_index)]
    right_side = key[int(end_index):]
    key = left_side + right_side
    return key



activation_key = input()
current_command = input()

while current_command != 'Generate':
    if current_command.startswith('Contains'):
        activation_key = contain_substring_check(activation_key, current_command)
    elif current_command.startswith('Flip'):
        activation_key = flip_case(activation_key, current_command)
        print(activation_key)
    elif current_command.startswith('Slice'):
        activation_key = slice_key(activation_key, current_command)
        print(activation_key)
    current_command = input()

print(f"Your activation key is: {activation_key}")