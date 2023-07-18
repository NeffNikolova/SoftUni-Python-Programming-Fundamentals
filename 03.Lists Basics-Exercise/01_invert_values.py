input_string = input()

original_list = []
opposite_list = []
for item in input_string.split():
    original_list.append(int(item))
for item in original_list:
    new_item = -int(item)
    opposite_list.append(new_item)

print(opposite_list)

