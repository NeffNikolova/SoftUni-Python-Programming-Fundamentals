list_of_characters = input().split(', ')
dictionary = {letter: ord(letter) for letter in list_of_characters}
print(dictionary)