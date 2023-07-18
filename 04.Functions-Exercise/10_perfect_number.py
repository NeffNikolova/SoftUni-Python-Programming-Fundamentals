def aliquot_sum_check(number:int) -> bool:
    perfect_number = False
    aliquot_sum = 0
    for num in range(1, number):
        if number % num == 0:
            aliquot_sum += num
    if aliquot_sum == number:
        perfect_number = True
        return perfect_number
    else:
        perfect_number = False
        return perfect_number


current_number = int(input())
if aliquot_sum_check(current_number):
    print(f"We have a perfect number!")
else:
    print("It's not so perfect.")

