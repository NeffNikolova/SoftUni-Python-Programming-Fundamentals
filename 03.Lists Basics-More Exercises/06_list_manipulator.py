initial_list = input().split()
initial_list = list(map(int, initial_list))
command = input()

first_half = []
second_half = []
current_list = []
filtered = []
match_found = False

while command != 'end':
    command_list = command.split()
    command_name = command_list[0]
    if command_name == 'exchange':
        initial_list = list(map(str, initial_list))
        command_index = int(command_list[1])
        if 0 <= command_index <= len(initial_list) - 1:
            first_half = initial_list[command_index + 1:]
            second_half = initial_list[:command_index + 1]
            initial_list = first_half + second_half
        else:
            print('Invalid index')
    elif command_name == 'max':
        initial_list = list(map(int, initial_list))
        command_value = command_list[1]
        current_list.extend(initial_list)
        current_list.sort(reverse=True)
        if command_value == 'odd':
            for value in current_list:
                if int(value) % 2 != 0:
                    print((len(initial_list) - 1 - initial_list[::-1].index(value)))
                    break
            else:
                print('No matches')
        elif command_value == 'even':
            for value in current_list:
                if int(value) % 2 == 0:
                    print((len(initial_list) - 1 - initial_list[::-1].index(value)))
                    break
            else:
                print('No matches')
        current_list = []
    elif command_name == 'min':
        initial_list = list(map(int, initial_list))
        command_value = command_list[1]
        current_list.extend(initial_list)
        current_list.sort()
        if command_value == 'odd':
            for value in current_list:
                if int(value) % 2 != 0:
                    print((len(initial_list) - 1 - initial_list[::-1].index(value)))
                    break
            else:
                print('No matches')
        elif command_value == 'even':
            for value in current_list:
                if int(value) % 2 == 0:
                    print((len(initial_list) - 1 - initial_list[::-1].index(value)))
                    break
            else:
                print('No matches')
        current_list = []
    elif command_name == 'first':
        initial_list = list(map(int, initial_list))
        command_value = command_list[1]
        command_description = command_list[2]
        if int(command_value) <= len(initial_list):
            for element in initial_list:
                if command_description == 'even':
                    if element % 2 == 0:
                        if len(filtered) < int(command_value):
                            filtered.append(element)
                        else:
                            break
                elif command_description == 'odd':
                    if element % 2 != 0:
                        if len(filtered) < int(command_value):
                            filtered.append(element)
                        else:
                            break
            print(filtered)
            filtered.clear()
        else:
            print('Invalid count')
    elif command_name == 'last':
        initial_list = list(map(int, initial_list))
        command_value = command_list[1]
        command_description = command_list[2]
        current_list = list(initial_list)
        current_list.reverse()
        if int(command_value) <= len(initial_list):
            for element in current_list:
                if command_description == 'even':
                    if element % 2 == 0:
                        if len(filtered) < int(command_value):
                            filtered.append(element)
                        else:
                            break
                elif command_description == 'odd':
                    if element % 2 != 0:
                        if len(filtered) < int(command_value):
                            filtered.append(element)
                        else:
                            break
            filtered.reverse()
            print(filtered)
            filtered.clear()
        else:
            print('Invalid count')
    command = input()

initial_list = list(map(int, initial_list))
print(initial_list)