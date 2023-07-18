first_string = input()
second_string = input()

new_string = ''
last_string = first_string

for i in range(len(first_string)):
    new_string = second_string[:i+1]+first_string[i+1:]
    if last_string == new_string:
        continue
    print(new_string)
    last_string = new_string
