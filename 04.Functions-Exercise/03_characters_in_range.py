def characters_in_range(start:str, end:str) -> list:
    range_characters = []
    for character in range(ord(start)+1, ord(end)):
        range_characters.append(chr(character))

    return range_characters


start_character = input()
end_character = input()

print(' '.join(characters_in_range(start_character, end_character)))
