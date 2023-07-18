input_string = input().split()
output = 0

for element in input_string:
    number = int(element[1:-1])

    if 65 <= ord(element[0]) <= 90:
        number /= (ord(element[0]) - 64)
    elif 97 <= ord(element[0]) <= 122:
        number *= (ord(element[0]) - 96)

    if 65 <= ord(element[-1]) <= 90:
        number -= (ord(element[-1]) - 64)
    elif 97 <= ord(element[-1]) <= 122:
        number += (ord(element[-1]) - 96)

    output += number
print(f'{output:.2f}')
