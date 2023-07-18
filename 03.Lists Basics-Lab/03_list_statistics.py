number_ot_integers = int(input())

positive_numbers = []
negative_numbers = []


for number in range(number_ot_integers):
    current_integer = int(input())

    if current_integer >= 0:
        positive_numbers.append(current_integer)
    else:
        negative_numbers.append(current_integer)

print(f'{positive_numbers}\n{negative_numbers}\nCount of positives: {len(positive_numbers)}'
      f'\nSum of negatives: {sum(negative_numbers)}')
