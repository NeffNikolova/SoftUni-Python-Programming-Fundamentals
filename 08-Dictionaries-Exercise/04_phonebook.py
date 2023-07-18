console_entry = input().split('-')
phonebook = {}

while len(console_entry) == 2:
    phonebook[console_entry[0]] = console_entry[1]
    console_entry = input().split('-')
else:
    for i in range(0, int(console_entry[0])):
        search = input()
        if phonebook.get(search) is None:
            print(f'Contact {search} does not exist.')
        else:
            print(f'{search} -> {phonebook[search]}')