import re

text = input()
output = []
while text:
    regex = r"(www[.][a-zA-Z0-9]*[a-zA-Z0-9-]*[.a-z]*[.][a-z]+)"
    matches = re.search(regex, text)
    if matches:
        output.append(matches.group(1))
    text = input()

for item in output:
    print(item)


