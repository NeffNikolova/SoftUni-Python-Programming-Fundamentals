
def merge(string_list, command):
    start = int(command[1])
    end = int(command[2])
    if int(end) > len(string_list) - 1:
        end = len(string_list) - 1
    if int(start) < 0:
        start = 0
    string_list[int(start):int(end)+1] = [''.join(string_list[int(start):int(end)+1])]
    return string_list


def divide(lst, command):
    index = int(command[1])
    element_to_divide = lst.pop(index)
    partitions = int(command[2])
    if len(element_to_divide) % partitions == 0:
        step = int(len(element_to_divide) / partitions)
        res = [element_to_divide[i:i + step] for i in range(0, len(element_to_divide), step)]
    else:
        step = int(len(element_to_divide) // partitions)
        res = [element_to_divide[i:i + step] for i in range(0, len(element_to_divide), step) if i < partitions-1]
        res.append(''.join(element_to_divide[partitions*step-1:]))

    for el in res[::-1]:
        lst.insert(index, el)
    return lst


start_string = input().split()
current_command = input()

while current_command != '3:1':
    command_list = current_command.split()
    if command_list[0] == 'merge':
        start_string = merge(start_string, command_list)
    elif command_list[0] == 'divide':
        start_string = divide(start_string, command_list)

    current_command = input()
else:
    print(' '.join(start_string))


