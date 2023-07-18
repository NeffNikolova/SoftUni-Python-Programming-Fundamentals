people_waiting = int(input())
lift_state = input().split()
lift_state = [int(el) for el in lift_state]
free_spots_in_wagon = 0
for index, el in enumerate(lift_state):

    if people_waiting > 0 and el < 4:
        free_spots_in_wagon = 4 - int(el)
        lift_state[index] = lift_state[index] + free_spots_in_wagon if free_spots_in_wagon < people_waiting \
            else lift_state[index] + people_waiting
        people_waiting -= free_spots_in_wagon if free_spots_in_wagon < people_waiting else people_waiting

if people_waiting == 0 and any([el for el in lift_state if el < 4]):
    print('The lift has empty spots!')
    print(*lift_state, sep=' ')
elif people_waiting > 0 and all([el for el in lift_state if el == 4]):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_state, sep=' ')
elif people_waiting == 0 and all([el for el in lift_state if el == 4]):
    print(*lift_state, sep=' ')



