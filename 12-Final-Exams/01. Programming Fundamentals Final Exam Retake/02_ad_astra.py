import re

text = input()
total_calories = 0
days = 0
pattern = r'([#||])([A-Z][a-z]+[ ]*[A-Z]?[a-z]*)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]{1,})\1'
matches = re.findall(pattern, text)
for match in matches:
    total_calories += int(match[3])
days += total_calories // 2000
print(f'You have food to last you for: {days} days!')
for match in matches:
    print(f'Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}')
