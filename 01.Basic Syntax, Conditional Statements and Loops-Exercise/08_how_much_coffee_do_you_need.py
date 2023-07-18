command = input()

total_coffees = 0
while command != 'END':
    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' or command.lower() == 'movie':
        if 97 <= ord(command[1]) <= 122:
            total_coffees += 1
        elif 65 <= ord(command[1]) <= 90:
            total_coffees += 2

    command = input()

if total_coffees > 5:
    print('You need extra sleep')
else:
    print(total_coffees)