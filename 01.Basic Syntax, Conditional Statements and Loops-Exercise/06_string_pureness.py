strings_number = int(input())

unpure_symbols = ',._'
unpure = False
for i in range(strings_number):
    current_string = input()
    for j in range(len(current_string)):
        if current_string[j] in unpure_symbols:
            unpure = True
    if unpure:
        print(f'{current_string} is not pure!')
        unpure = False
    else:
        print(f'{current_string} is pure.')
