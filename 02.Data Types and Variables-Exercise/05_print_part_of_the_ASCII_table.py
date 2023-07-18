start_index = int(input())
last_index = int(input())

output = ''
for index in range(start_index, last_index + 1):
    character = chr(index)
    output += character + ' '

print(output)