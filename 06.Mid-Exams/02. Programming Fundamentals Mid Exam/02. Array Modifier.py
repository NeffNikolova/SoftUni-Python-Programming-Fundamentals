def swap(some_list, index1_list, index2_list):
    index1_list, index2_list = int(index1_list), int(index2_list)
    some_list[index1_list], some_list[index2_list] = some_list[index2_list], some_list[index1_list]
    return some_list


def multiply(some_list, index1_list, index2_list):
    index1_list, index2_list = int(index1_list), int(index2_list)
    some_list[index1_list] = some_list[index1_list] * some_list[index2_list]
    return some_list


array_values = input().split()
array_values = [int(element) for element in array_values]
command = input()

while command != 'end':
    if 'swap' in command:
        operation, index1, index2 = command.split()
        array_values = swap(array_values, index1, index2)
    elif 'multiply' in command:
        operation, index1, index2 = command.split()
        array_values = multiply(array_values, index1, index2)
    elif 'decrease' in command:
        array_values = [(lambda x: x-1)(x) for x in array_values]

    command = input()

print(*array_values, sep=', ')