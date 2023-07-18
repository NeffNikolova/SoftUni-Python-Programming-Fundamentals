def number_sorter(max_number, numbers_list):
    return [num for num in numbers_list if num <= max_number]


all_numbers_original = input().split(', ') # max = 55
all_numbers_original = [int(num) for num in all_numbers_original]
if max(all_numbers_original)%10 == 0:
    nr_groups = (max(all_numbers_original) // 10)
else:
    nr_groups = (max(all_numbers_original) // 10) + 1
all_numbers = all_numbers_original
max_number_current_group = 10

for group in range(nr_groups):
    current_group = list(number_sorter(max_number_current_group,all_numbers))
    print(f"Group of {max_number_current_group}'s: {current_group}")
    all_numbers = [num for num in all_numbers if num not in current_group]
    current_group.clear()
    max_number_current_group += 10
    if max_number_current_group > nr_groups * 10:
        break









