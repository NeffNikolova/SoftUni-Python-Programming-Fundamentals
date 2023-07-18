groceries_list = input().split('!')
command = input()

while command != 'Go Shopping!':

    if 'Urgent' in command:
        action, item = command.split()
        if item not in groceries_list:
            groceries_list.insert(0, item)
    elif 'Unnecessary' in command:
        action, item = command.split()
        if item in groceries_list:
            groceries_list.remove(item)
    elif 'Correct' in command:
        action, old_item, new_item = command.split()
        if old_item in groceries_list:
            groceries_list[(groceries_list.index(old_item))] = new_item
    elif 'Rearrange' in command:
        action, item = command.split()
        if item in groceries_list:
            groceries_list.append(groceries_list.pop(groceries_list.index(item)))
    command = input()

print(*groceries_list, sep=', ')
