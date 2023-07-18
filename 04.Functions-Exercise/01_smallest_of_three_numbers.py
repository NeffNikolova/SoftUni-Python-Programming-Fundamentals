def smallest_number(first:int, second:int, third:int) -> int:
    result = None
    if first < second and first < third:
        result = first
    elif second < first and second < third:
        result = second
    elif third < first and third < second:
        result = third
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number, second_number, third_number))
