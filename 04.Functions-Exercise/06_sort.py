def sorter(some_list:list) -> list:
    some_list = list(map(int,some_list))
    return sorted(some_list)


list_of_numbers = input().split()

print(sorter(list_of_numbers))
