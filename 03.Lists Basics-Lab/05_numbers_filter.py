number_of_integers = int(input())

all_numbers_list = []
filtered_list = []

for number in range(number_of_integers):
    current_integer = int(input())
    all_numbers_list.append(current_integer)

command = input()
if command == 'even':
    for element in all_numbers_list:
        if element % 2 == 0:
            filtered_list.append(element)
elif command == 'odd':
    for element in all_numbers_list:
        if element % 2!= 0:
            filtered_list.append(element)
elif command == 'negative':
    for element in all_numbers_list:
        if element < 0:
            filtered_list.append(element)
elif command == 'positive':
    for element in all_numbers_list:
        if element >= 0:
            filtered_list.append(element)

print(filtered_list)

