daily_decorations_quantity = int(input())
days = int(input())

ornament_set_pr = 2
ornament_set_pts = 5
tree_skirt_pr = 5
tree_skirt_pts = 3
tree_garland_pr = 3
tree_garland_pts = 10
tree_lights_pr = 15
tree_lights_pts = 17

spirit = 0
total_cost = 0

for current_day in range(1, days + 1):

    if current_day % 11 == 0:
        daily_decorations_quantity += 2

    if current_day % 2 == 0:
        total_cost += daily_decorations_quantity*ornament_set_pr
        spirit += ornament_set_pts

    if current_day % 3 == 0:
        total_cost += daily_decorations_quantity * (tree_skirt_pr + tree_garland_pr)
        spirit += tree_skirt_pts + tree_garland_pts

    if current_day % 5 == 0:
        total_cost += daily_decorations_quantity * tree_lights_pr
        spirit += tree_lights_pts
        if current_day % 3 == 0:
            spirit += 30

    if current_day % 10 == 0:
        spirit -= 20
        total_cost += tree_skirt_pr + tree_garland_pr + tree_lights_pr
        if days == current_day:
            spirit -= 30


print(f"Total cost: {total_cost}")
print(f'Total spirit: {spirit}')