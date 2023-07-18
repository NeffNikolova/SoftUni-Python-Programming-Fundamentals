def add_and_subtract(first:int,second:int,third:int) -> int:

    def sum_numbers(first_n: int, second_n: int) -> int:
        result_sum = first_n + second_n
        return result_sum

    def subtract(sum_first_second: int, third_n: int) -> int:
        result_subtract = sum_first_second - third_n
        return result_subtract

    return subtract(sum_numbers(first, second), third)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))