import re

text = input()
pairs = {}
mirror_pairs = []
pattern = r"([@|#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.findall(pattern, text)
for match in matches:
    pairs[match[1]] = match[2]

for key, value in pairs.items():
    if key[::-1] == value:
        current_pair = f'{key} <=> {value}'
        mirror_pairs.append(current_pair)
if pairs:
    print(f'{len(pairs)} word pairs found!')
else:
    print("No word pairs found!")

if mirror_pairs:
    print('The mirror words are:')
    print(*mirror_pairs, sep=', ')
else:
    print('No mirror words!')
