farmed_items = (input().lower()).split()
junk = {}
materials = {'shards': 0, 'fragments': 0, 'motes': 0}
win = False

while not win:
    for index in range(0, len(farmed_items), 2):
        if farmed_items[index+1] in materials:
            materials[farmed_items[index+1]] += int(farmed_items[index])
        else:
            if farmed_items[index+1] not in junk:
                junk[farmed_items[index+1]] = 0
            junk[farmed_items[index+1]] += int(farmed_items[index])

        if materials['shards'] >= 250:
            print('Shadowmourne obtained!')
            materials['shards'] -= 250
            win = True
            break
        elif materials['fragments'] >= 250:
            print('Valanyr obtained!')
            materials['fragments'] -= 250
            win = True
            break
        elif materials['motes'] >= 250:
            print('Dragonwrath obtained!')
            materials['motes'] -= 250
            win = True
            break
    if not win:
        farmed_items.clear()
        farmed_items = (input().lower()).split()

for key, value in materials.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')
