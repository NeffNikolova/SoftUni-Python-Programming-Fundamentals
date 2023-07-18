def calculate_order_price(product:str, quantity:int) -> float:
    order_price = 0.00
    if product == 'coffee':
        order_price = quantity * 1.5
    elif product == 'water':
        order_price = quantity * 1.0
    elif product == 'coke':
        order_price = quantity * 1.40
    elif product == 'snacks':
        order_price = quantity * 2.00

    return order_price


ordered_product = input()
ordered_quantity = int(input())

print(f'{calculate_order_price(ordered_product,ordered_quantity):.2f}')
