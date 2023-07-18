string = input()
chars = {}

for letter in string:
    if letter != ' ':
        if letter not in chars:
            chars[letter] = 0
        chars[letter] += 1

for key,value in chars.items():
    print(f'{key} -> {value}')