integer_list = input().split(', ')
integer_list = list(map(int, integer_list))

for value in integer_list:
    # add to the end of the list the removed instance for the index of the first encountered value of ZERO
    integer_list.append(integer_list.pop(integer_list.index(0)))
print(integer_list)
