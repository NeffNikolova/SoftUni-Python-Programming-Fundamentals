product_to_add = input()
statistics = {}

while product_to_add != 'statistics':
    product, quantity = product_to_add.split(':')
    quantity = int(quantity)
    if product not in statistics.keys():
        statistics[product] = 0
    statistics[product] += quantity

    product_to_add = input()
else:
    print("Products in stock:")
    for product, quantity in statistics.items():
        print(f"- {product}: {quantity}")
    print(f"Total Products: {len(statistics.keys())}\nTotal Quantity: {sum(statistics.values())}")
