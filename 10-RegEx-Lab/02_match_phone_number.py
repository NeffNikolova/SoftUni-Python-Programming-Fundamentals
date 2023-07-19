import re

numbers_to_check = input()
regex = "(\\+359-2-[0-9]{3}-[0-9]{4}\\b|\\+359 2 [0-9]{3} [0-9]{4})\\b"
matches = re.findall(regex, numbers_to_check)
print(", ".join(matches))
