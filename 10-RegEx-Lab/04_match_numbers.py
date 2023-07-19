import re

dates_to_check = input()

regex = r"(^|(?<=\s))-?([0]|[1-9]\d*)(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, dates_to_check)
for match in matches:
    print(match.group(), end=' ')
