import re

number_of_entries = int(input())
pattern = re.compile(r'[|](?P<name>[A-Z]{4,})[|][:][#](?P<title>[A-Za-z]+[ ][A-Za-z]+)[#]')

for number in range(number_of_entries):
    current_entry = input()
    match = re.search(pattern, current_entry)
    if match:
        print(f'{match.group("name")}, The {match.group("title")}')
        print(f'>> Strength: {len(match.group("name"))}')
        print(f'>> Armor: {len(match.group("title"))}')
    else:
        print("Access denied!")

