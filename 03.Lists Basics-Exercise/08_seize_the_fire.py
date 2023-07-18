fire_info = input()
water = int(input())


cell_fire = fire_info.split('#')
cell_valid = False
put_out_cells = []
total_effort = 0

for cell in cell_fire:
    type_of_fire, cell_value = cell.split(' = ')
    if (type_of_fire == 'High' and 81 <= int(cell_value) <= 125) \
            or (type_of_fire == 'Medium' and 51 <= int(cell_value) <= 80) \
            or (type_of_fire == 'Low' and 1 <= int(cell_value) <= 50):
        cell_valid = True

    if cell_valid and water >= int(cell_value):
        water -= int(cell_value)
        put_out_cells.append(int(cell_value))
        total_effort += (int(cell_value) * 0.25)
    else:
        continue

    cell_valid = False

total_fire = sum(put_out_cells)
put_out_cells = map(str, put_out_cells)
printable_list = '\n - '.join(put_out_cells)
print(f'Cells:\n - {printable_list}\nEffort: {total_effort:.2f}\nTotal Fire: {total_fire}')