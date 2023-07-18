to_do = ['0'] * 10

command = input().split('-')

while command[0] != 'End':
    to_do.pop((int(command[0])) - 1)
    to_do.insert(int(command[0]) - 1, command[1])
    command = input().split('-')

print([task for task in to_do if task != '0'])


