import re

text = input()
destinations = []
points = 0
pattern = r'([=|/])([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, text)
for match in matches:
    destinations.append(match[1])
    points += len(match[1])

print('Destinations: ', end='')
print(', '.join(destinations))
print(f'Travel Points: {points}')

