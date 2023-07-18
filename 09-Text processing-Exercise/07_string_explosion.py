input_string = input()
output = ''

explosion_strength = 0

for index in range(len(input_string)):

    if input_string[index] == '>':
        explosion_strength += int(input_string[index + 1])
        output += input_string[index]
    elif explosion_strength == 0:
        output += input_string[index]
    else:
        explosion_strength -= 1
        continue
print(output)




