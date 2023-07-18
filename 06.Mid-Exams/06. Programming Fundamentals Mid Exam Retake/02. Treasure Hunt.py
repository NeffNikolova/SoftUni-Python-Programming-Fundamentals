initial_loot = input().split('|')
command = input()

sum_len = 0

while command != 'Yohoho!':
    if 'Loot' in command:
        items = command.split()
        items.pop(0)
        for item in items:
            if item not in initial_loot:
                initial_loot.insert(0, item)
    elif 'Drop' in command:
        action, position = command.split()
        position = int(position)
        if 0 <= position < len(initial_loot):
            initial_loot.append(initial_loot.pop(position))
    elif 'Steal' in command:
        action, count = command.split()
        stolen_items = []
        for item in initial_loot[::-1]:
            if len(stolen_items) < int(count):
                stolen_items.append(initial_loot.pop(initial_loot.index(item)))
        print(*stolen_items[::-1], sep=', ')
    command = input()
if initial_loot:
    for item in initial_loot:
        sum_len += len(item)
    print(f"Average treasure gain: {(sum_len/len(initial_loot)):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")