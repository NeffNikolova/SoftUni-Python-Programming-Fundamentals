number_of_lines = int(input())

nr_brackets = 0
last_bracket = ''
balanced = True

for line in range(number_of_lines):
    input_string = input()

    if input_string == '(' or input_string == ')':
        nr_brackets += 1
        if nr_brackets == 1 and input_string == ')':
            balanced = False
            break
        elif nr_brackets == 1:
            last_bracket = input_string
        elif nr_brackets > 1:
            if (last_bracket == '(' and input_string == '(') or (last_bracket == ')' and input_string == ')'):
                balanced = False
            last_bracket = input_string
if nr_brackets % 2 != 0:
    balanced = False

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')






