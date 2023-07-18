orders_number = int(input())

total_price = 0
for i in range(orders_number):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        print(f'The price for the coffee is: ${(price_per_capsule * capsules_per_day * days):.2f}')
        total_price += (price_per_capsule * capsules_per_day * days)
    else:
        continue
print(f'Total: ${total_price:.2f}')


