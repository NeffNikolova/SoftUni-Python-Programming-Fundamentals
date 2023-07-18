original_list = input().split(', ')
original_list = [int(el) for el in original_list]
positive_list = [el for el in original_list if el >= 0]
negative_list = [el for el in original_list if el < 0]
even_list = [el for el in original_list if el % 2 == 0]
odd_list = [el for el in original_list if el % 2 != 0]

print('Positive: ', end='')
print(*positive_list, sep=', ')
print('Negative: ', end='')
print(*negative_list, sep=', ')
print('Even: ', end='')
print(*even_list, sep=', ')
print('Odd: ', end='')
print(*odd_list, sep=', ')