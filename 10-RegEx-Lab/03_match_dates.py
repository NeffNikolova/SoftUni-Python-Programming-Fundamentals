import re

dates_to_check = input()

regex = r"\b(\d{2})([/.-])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(regex, dates_to_check)
for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
