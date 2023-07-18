items_for_sale = input().split('|')
start_budget = float(input())

new_item_prices = []
profit = 0

for item in items_for_sale:
    item_type, item_price = item.split('->')
    item_price = float(item_price)

    if ((item_type == 'Clothes' and item_price <= 50) or
        (item_type == 'Shoes' and item_price <= 35) or
        (item_type == 'Accessories' and item_price <= 20.50)) and start_budget >= item_price:
        start_budget -= item_price

        new_item_price = 1.40 * item_price
        new_item_prices.append(float(new_item_price))
        profit += new_item_price - item_price

for new_price in new_item_prices:
    print(f"{new_price:.2f}", end=" ")
print()

print(f'Profit: {profit:.2f}')

if sum(new_item_prices) + start_budget >= 150:
    print('Hello, France!')
else:
    print("Not enough money.")

