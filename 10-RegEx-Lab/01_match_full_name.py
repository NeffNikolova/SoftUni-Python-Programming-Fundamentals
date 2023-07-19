import re

names_to_test = input()
regex = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(regex, names_to_test)
print(" ".join(matches))