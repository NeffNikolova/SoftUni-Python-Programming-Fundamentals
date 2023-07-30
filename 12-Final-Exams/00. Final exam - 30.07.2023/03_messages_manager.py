def add_user(database, command):
    action, user, sent, received = command.split('=')
    if user not in database:
        database[user] = [int(sent), int(received)]
    return database


def send_message(database, command, max_messages):
    action, sender, receiver = command.split('=')
    if sender in database and receiver in database:
        database[sender][0] += 1
        database[receiver][0] += 1
        if int(database[sender][0]) + int(database[sender][1]) == int(max_messages):
            del database[sender]
            print(f'{sender} reached the capacity!')
        if int(database[receiver][0]) + int(database[receiver][1]) == int(max_messages):
            del database[receiver]
            print(f'{receiver} reached the capacity!')
    return database


def empty(database, command):
    action, user = command.split('=')
    if user == 'All':
        database.clear()
    else:
        database[user].clear()
    return database


message_capacity = int(input())
current_command = input()

messages_database = {}

while current_command != 'Statistics':
    if current_command.startswith('Add'):
        messages_database = add_user(messages_database, current_command)
    elif current_command.startswith('Message'):
        messages_database = send_message(messages_database, current_command, message_capacity)
    elif current_command.startswith('Empty'):
        messages_database = empty(messages_database, current_command)

    current_command = input()

final_database = {key: value for (key, value) in messages_database.items() if value}
print(f'Users count: {len(final_database)}')
for key,value in final_database.items():
    print(f'{key} - {sum(value)}')