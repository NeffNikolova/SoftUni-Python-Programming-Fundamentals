def create_new_side(force_side: str, force_user: str, dct: dict, printable: bool):
    dct[force_side] = []
    dct[force_side].append(force_user)
    if printable:
        print(f"{force_user} joins the {force_side} side!")
    else:
        return dct


def add_to_existing_side(force_side: str, force_user: str, dct: dict, printable: bool):
    dct[force_side].append(force_user)
    if printable:
        print(f"{force_user} joins the {force_side} side!")
    else:
        return dct


command = input()
sides = {}
arrow = False

while command != 'Lumpawaroo':
    if '|' in command:
        side, user = command.split(' | ', 1)
        arrow = False
    else:
        user, side = command.split(' -> ', 1)
        arrow = True

    if side not in sides.keys() and not any(user in val for val in sides.values()):
        create_new_side(side, user, sides, arrow)
        # sides[side] = []
        # sides[side].append(user)
        # if arrow:
        #     print(f"{user} joins the {side} side!")
    elif side in sides.keys() and not any(user in val for val in sides.values()):
        add_to_existing_side(side, user, sides, arrow)
        # sides[side].append(user)
        # if arrow:
        #     print(f"{user} joins the {side} side!")
    elif any(user in val for val in sides.values()) and not arrow:
        pass
    elif any(user in val for val in sides.values()) and arrow:
        for key in list(sides.keys()):
            if key != side and user in sides[key]:
                sides[side].append(sides[key].pop(sides[key].index(user)))
                if arrow:
                    print(f"{user} joins the {side} side!")
    command = input()

for key, value in sides.items():
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        for val in value:
            print(f'! {val}')





