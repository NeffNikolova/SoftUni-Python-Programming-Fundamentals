food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
guinea_pig_weight = float(input())

not_enough = False
for day in range(1, 31):
    food_kg -= 0.300
    if day % 2 == 0:
        hay_kg -= (0.05 * food_kg)
    if day % 3 == 0:
        cover_kg -= (1/3 * guinea_pig_weight)
    if round(food_kg,2) <= 0 or round(hay_kg, 2) <= 0 or round(cover_kg, 2) <= 0:
        not_enough = True
        break

if not_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
