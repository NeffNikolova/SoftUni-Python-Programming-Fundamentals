elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    bakery[elements[index]] = int(elements[index+1])

print(bakery)