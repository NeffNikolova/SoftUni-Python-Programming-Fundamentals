budget = int(input())
price = input()

while price != 'End':
    price = int(price)
    if budget < price:
        print('You went in overdraft!')
        break
    else:
        budget -= price
        price = input()
else:
    print('You bought everything needed.')
