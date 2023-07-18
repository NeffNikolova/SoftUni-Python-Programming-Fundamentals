names_of_gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    if command[0] == 'OutOfStock':
        names_of_gifts = [string.replace(command[1], 'None') for string in names_of_gifts]
    elif command[0] == 'Required':
        if 0 < int(command[2]) <= len(names_of_gifts)-1:
            names_of_gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        names_of_gifts[-1] = command[1]
    command = input()

for element in names_of_gifts[:-1]:
    if element != 'None':
        print(element, end=' ')
if names_of_gifts[-1] != 'None':
    print(names_of_gifts[-1])
