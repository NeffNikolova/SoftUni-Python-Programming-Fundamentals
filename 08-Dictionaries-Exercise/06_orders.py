command = input().split()
products = {}

while len(command) > 1:
    product, price, quantity = command[0], command[1], command[2]

    if product not in products:
        products[product] = []
        products[product].append(0)
        products[product].append(0)
    products[product][0] = float(price)
    products[product][1] += int(quantity)
    command = input().split()

for key, value in products.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')