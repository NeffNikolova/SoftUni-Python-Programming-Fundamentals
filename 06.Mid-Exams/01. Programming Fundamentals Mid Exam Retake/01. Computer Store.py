command = input()

invalid_order = False
total_net_price = 0
total_tax = 0
total = 0

while command != 'regular' and command != 'special':
    net_price = float(command)

    if net_price <= 0:
        print('Invalid price!')
    else:
        total_net_price += net_price

    command = input()

if total_net_price == 0:
    invalid_order = True

total_tax = 0.2 * total_net_price
if command == 'special':
    total = (total_net_price + total_tax) * 0.9
else:
    total = (total_net_price + total_tax)

if invalid_order:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without "
          f"taxes: {total_net_price:.2f}$\nTaxes: {total_tax:.2f}$\n"
          f"-----------\nTotal price: {total:.2f}$")

