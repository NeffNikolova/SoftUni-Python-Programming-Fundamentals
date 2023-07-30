import re

text = input()
cool_emojis = []
current_coolness = 0
emoji_count = 0
pattern = r'([\:{2}|\*]{2})(?P<emoji>[A-Z][a-z]{2,})(\1)'
emojis = re.finditer(pattern, text)

cool_threshold = 1
digits = re.findall(r'\d', text)
for digit in digits:
    cool_threshold *= int(digit)

if emojis:
    for match in emojis:
        emoji_count += 1
        for letter in match.group("emoji"):
            current_coolness += ord(letter)
        if current_coolness > cool_threshold:
            cool_emojis.append(match.group())
        current_coolness = 0


print(f'Cool threshold: {cool_threshold}')
print(f'{emoji_count} emojis found in the text. The cool ones are:')
print('\n'.join([cool_emoji for cool_emoji in cool_emojis]))

