def shoot_target(some_list, target_index, power):
    if target_index < len(some_list):
        if some_list[target_index] > power:
            some_list[target_index] -= power
        else:
            some_list.pop(target_index)
    return some_list


def add_target(some_list, target_index, value_):
    if target_index < len(some_list):
        some_list.insert(target_index, value_)
    else:
        print('Invalid placement!')
    return some_list


def strike_target(some_list, target_index, value_):
    if 0 <= target_index + value_ < len(some_list) and 0 <= target_index - value_ < len(some_list):
        for ind in range(target_index + value_, target_index-value_-1,-1):
            some_list.pop(ind)
    else:
        print('Strike missed!')
    return some_list


target_sequence = input().split()
target_sequence = [int(el) for el in target_sequence]

command = input()

while command != 'End':
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if action == 'Shoot':
        target_sequence = shoot_target(target_sequence, index, value)
    elif action == 'Add':
        target_sequence = add_target(target_sequence, index, value)
    elif action == 'Strike':
        target_sequence = strike_target(target_sequence, index, value)

    command = input()
print(*target_sequence, sep='|')