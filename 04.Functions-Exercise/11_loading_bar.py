def loading_state(number:int) -> str:
    number = int(number/10)
    bar = ''
    dots_multipl = int(10-number)

    if number == 10:
        bar += '[%%%%%%%%%%]'
        return bar
    else:
        dots = '.' * dots_multipl
        percents = '%' * number
        bar += str(number) + '0%' + ' ' + '[' + percents + dots + ']'
        return bar


current_number = int(input())

if current_number == 100:
    print('100% Complete!')
    print(loading_state(current_number))
else:
    print(loading_state(current_number))
    print('Still loading...')

