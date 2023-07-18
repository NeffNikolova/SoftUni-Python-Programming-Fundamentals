def shoot_a_target(some_list, target, position: int, shot: list):
    some_list[position] = -1
    shot.append(target)
    for ind, el in enumerate(some_list):
        if el > target:
            some_list[ind] -= target
        elif el <= target and el != -1:
            some_list[ind] += target
    return some_list


sequence = input().split()
sequence = [int(element) for element in sequence]

action = input()
shot_targets = []
while action != 'End':
    index_to_shoot = int(action)
    if index_to_shoot < len(sequence):
        current_target = sequence[index_to_shoot]
    else:
        action = input()
        continue
    if current_target != -1:
        sequence = shoot_a_target(sequence, current_target, index_to_shoot, shot_targets)
    else:
        continue
    action = input()

print(f'Shot targets: {len(shot_targets)} -> ', end='')
print(*sequence, sep=' ')
