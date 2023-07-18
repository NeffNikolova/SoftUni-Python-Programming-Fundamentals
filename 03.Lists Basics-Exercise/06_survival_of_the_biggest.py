list_of_integers = input()
numbers_to_remove = int(input())

list_of_integers = list(map(int, list_of_integers.split()))

for number in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

for element in list_of_integers[:-1]:
    print(element, end = ', ')
print(list_of_integers[-1])