def absolute_value(some_list_of_numbers):
    """
    A function that receives a list of float numbers and calculates their absolute values.
    :return: A list of positive float numbers that represent the absolute values of the input
    """
    list_of_abs_values = []
    for each in some_list_of_numbers:
        list_of_abs_values.append(abs(float(each)))
    return list_of_abs_values


list_of_numbers = input().split()

print(absolute_value(list_of_numbers))
