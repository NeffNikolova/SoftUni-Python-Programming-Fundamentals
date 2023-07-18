def odd_and_even_sum(single_number:str):
    odd_nums = 0
    even_nums = 0

    for character in single_number:
        if int(character) % 2 ==0:
            even_nums += int(character)
        else:
            odd_nums += int(character)

    return even_nums, odd_nums


input_number = input()

even_digits, odd_digits = odd_and_even_sum(input_number)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")

