lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0

total_expenses += (lost_fights_count // 2) * helmet_price
total_expenses += (lost_fights_count // 3) * sword_price
total_expenses += (lost_fights_count // 6) * shield_price
total_expenses += ((lost_fights_count // 6) // 2) * armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")