factor = int(input())
count = int(input())

multiples_list = []

for multiplier in range(1, count + 1):
    current_number = multiplier * factor
    multiples_list.append(current_number)

print(multiples_list)
