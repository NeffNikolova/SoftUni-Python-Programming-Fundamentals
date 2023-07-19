import re

text = input()
word = input()

regex = r"\b" + word.lower() + r"\b"
matches = re.findall(regex, text.lower())
print(len(matches))