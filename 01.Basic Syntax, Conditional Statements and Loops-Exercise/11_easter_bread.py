budget = float(input())
flour_price_kg = float(input())

eggs_price = 0.75 * flour_price_kg
milk_price_250 = (1.25 * flour_price_kg)/4

eggs_nr = 0
breads_nr = 0
i = 0
while True:
    i += 1
    if budget > (milk_price_250 + flour_price_kg + eggs_price):
        budget -= (milk_price_250 + flour_price_kg + eggs_price)
    else:
        break

    breads_nr += 1
    eggs_nr += 3

    if breads_nr % 3 == 0:
        eggs_nr -= (breads_nr - 2)

print(f"You made {breads_nr} loaves of Easter bread! Now you have {eggs_nr} eggs and {budget:.2f}BGN left.")


