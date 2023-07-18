def rounding_lists(list_of_values:list) -> list:
    rounded_list = []
    for value in list_of_values:
        rounded_list.append(round(float(value)))
    return rounded_list


numbers_to_round = input().split()
print(rounding_lists(numbers_to_round))