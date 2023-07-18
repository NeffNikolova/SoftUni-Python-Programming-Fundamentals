execution_list = input().split()
permutation_factor = int(input())

start_index = 0
order_of_execution = []
current_index = 0

while len(execution_list) > 0:
    if start_index == len(execution_list):
        start_index = 0
    if start_index == len(execution_list) - 1:
        start_index = -1

    if start_index + permutation_factor - 1 < len(execution_list):
        current_index = start_index + permutation_factor-1
        order_of_execution.append(execution_list.pop(current_index))
        if len(execution_list) == 0:
            break
        start_index = current_index
    elif start_index + permutation_factor - 1 >= len(execution_list):
        current_index = (start_index + permutation_factor - 1) % len(execution_list)
        order_of_execution.append(execution_list.pop(current_index))
        if len(execution_list) == 0:
            break
        start_index = current_index

order_of_execution = ','.join(order_of_execution)
print(f'[' + order_of_execution + ']')


