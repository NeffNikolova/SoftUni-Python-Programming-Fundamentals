def collect_item(lst, element):
    if element not in lst:
        lst.append(element)
    return lst


def drop_item(lst, element):
    if element in lst:
        lst.pop(lst.index(element))
    return lst


def combine_items(lst:list, element):
    item1, item2 = element.split(':')
    if item1 in lst:
        lst.insert((lst.index(item1) + 1), item2)
    return lst


def renew_list(lst, element):
    if element in lst:
        lst.append(lst.pop(lst.index(element)))
    return lst


inventory = input().split(', ')
command = input()

while command != 'Craft!':
    action, item = command.split(' - ')
    if action == 'Collect':
        inventory = collect_item(inventory, item)
    elif action == 'Drop':
        inventory = drop_item(inventory, item)
    elif action == 'Combine Items':
        inventory = combine_items(inventory, item)
    elif action == 'Renew':
        inventory = renew_list(inventory, item)
    command = input()
else:
    print(*inventory, sep=', ')
