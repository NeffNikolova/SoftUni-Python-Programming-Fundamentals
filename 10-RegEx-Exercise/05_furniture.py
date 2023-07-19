import re

text = input()
regex = r'>>([a-zA-Z]+)<<(\d+[.]?\d*)!(\d+)'
furniture = []
total_price = 0
while text != 'Purchase':
    matches = re.search(regex, text)
    if matches:
        furniture.append(matches.group(1))
        total_price += float(matches.group(2)) * int(matches.group(3))
    text = input()

print("Bought furniture:")
for item in furniture:
    print(item)
print(f'Total money spend: {total_price:.2f}')