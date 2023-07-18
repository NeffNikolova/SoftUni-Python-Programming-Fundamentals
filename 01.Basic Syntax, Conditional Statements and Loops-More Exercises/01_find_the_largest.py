number = int(input())
# convert input string elements to list:
res_list = [int(x) for x in str(number)]
# sort list in reverse:
x = sorted(res_list, reverse=True)
# print sorted list with no separator
for i in x:
    print(i, end='')