number_to_check = int(input())

divider = 0

for i in range(2, number_to_check + 1):
    if number_to_check % i == 0:
        divider += 1

if divider > 1:
    print('False')
else:
    print('True')
