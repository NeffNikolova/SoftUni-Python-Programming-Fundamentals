def add_phone(lst, action):
    phone_model = action.split(' - ')[1]
    if phone_model not in lst:
        lst.append(phone_model)
    return lst


def remove_phone(lst, action):
    phone_model = action.split(' - ')[1]
    if phone_model in lst:
        lst.remove(phone_model)
    return lst


def bonus_phone(lst, action):
    phones_for_bonus = action.split(' - ')[1]
    old_phone, new_phone = phones_for_bonus.split(':')
    if old_phone in lst:
        lst.insert(lst.index(old_phone) + 1, new_phone)
    return lst


def move_last(lst, action):
    phone_for_last = action.split(' - ')[1]
    if phone_for_last in lst:
        lst.append(lst.pop(lst.index(phone_for_last)))
    return lst


list_of_phones = input().split(', ')
command = input()

while command != 'End':
    if 'Add' in command:
        list_of_phones = add_phone(list_of_phones, command)
    elif 'Remove' in command:
        list_of_phones = remove_phone(list_of_phones, command)
    elif 'Bonus phone' in command:
        list_of_phones = bonus_phone(list_of_phones, command)
    elif 'Last' in command:
        list_of_phones = move_last(list_of_phones, command)

    command = input()
else:
    print(*list_of_phones, sep=', ')
