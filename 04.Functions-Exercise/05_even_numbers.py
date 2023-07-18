def even_numbers(list_numbers:list) -> list:
    list_even = []

    for number in list_numbers:
        if int(number) % 2 == 0:
            list_even.append(int(number))
    return list_even


list_current_numbers = input().split()
print(even_numbers(list_current_numbers))
