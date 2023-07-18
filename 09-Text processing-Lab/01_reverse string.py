command = input()
reversed_text = ''

while command != 'end':
    reversed_text = command[::-1]
    print(f'{command} = {reversed_text}')
    command = input()

