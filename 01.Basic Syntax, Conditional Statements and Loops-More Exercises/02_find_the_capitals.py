current_string = input()
# create empty list to store the output
output = []
# define starting position as -1 bcs 1st position in list has index 0
current_position = -1
# convert input string into list
res_list = [str(x) for x in str(current_string)]
# for each element of the list
for i in res_list:
    # each iteration of the list elements, moves the current position one up
    current_position += 1
    # check if Capital letter
    if 65 <= ord(i) <= 90:
        # return index of element in list starting to search from the defined position in list
        # index = res_list.index(i, current_position)
        # add current position index into empty output list
        output.append(current_position)
print(output)
