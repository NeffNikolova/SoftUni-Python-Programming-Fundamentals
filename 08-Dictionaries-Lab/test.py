input_information = input().split()
bakery = {}

for i in range(0, len(input_information)-1, 2):
    bakery[input_information[i]] = int(input_information[i+1])

print(bakery)
