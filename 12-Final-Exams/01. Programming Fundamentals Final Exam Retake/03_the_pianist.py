def add_piece(database, piece, composer, key):
    if piece not in database.keys():
        database[piece] = []
        database[piece].append(composer)
        database[piece].append(key)
        return f'{piece} by {composer} in {key} added to the collection!'
    else:
        return f'{piece} is already in the collection!'


def remove_piece(database, piece):
    if piece in database.keys():
        database.pop(piece)
        return f"Successfully removed {piece}!"
    else:
        return f"Invalid operation! {piece} does not exist in the collection."


def change_key(database, piece, new_key):
    if piece in database.keys():
        database[piece].pop(1)
        database[piece].append(new_key)
        return f'Changed the key of {piece} to {new_key}!'
    else:
        return f'Invalid operation! {piece} does not exist in the collection.'


number_of_pieces = int(input())
pieces_details = {}

for line in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split('|')
    pieces_details[current_piece] = []
    pieces_details[current_piece].append(current_composer)
    pieces_details[current_piece].append(current_key)

command = input()

while command != 'Stop':
    action = command.split('|')[0]
    if action == 'Add':
        print(add_piece(pieces_details, command.split('|')[1], command.split('|')[2], command.split('|')[3]))
    elif action == 'Remove':
        print(remove_piece(pieces_details, command.split('|')[1]))
    elif action == 'ChangeKey':
        print(change_key(pieces_details, command.split('|')[1], command.split('|')[2]))
    command = input()

for piece, details in pieces_details.items():
    print(f'{piece} -> Composer: {details[0]}, Key: {details[1]}')
