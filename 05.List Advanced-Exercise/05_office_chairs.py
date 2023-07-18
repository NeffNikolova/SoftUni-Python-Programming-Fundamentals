def room_checker(some_room):
    output = 0
    output = len(some_room[0]) - int(some_room[1])
    return output


number_of_rooms = int(input())
current_room = []
extra_chairs = []
for room in range(number_of_rooms):
    current_room = input().split()
    extra_chairs.append(room_checker(current_room))

if any(int(el) for el in extra_chairs if el < 0):
    extra_chairs_index = [str(index) for index, num in enumerate(extra_chairs) if num < 0]
    extra_chairs_values = [num for index, num in enumerate(extra_chairs) if num < 0]
    for i in range(len(extra_chairs_index)):
        print(f'{abs(extra_chairs_values[i])} more chairs needed in room {int(extra_chairs_index[i]) + 1}')
else:
    print(f'Game On, {sum(extra_chairs)} free chairs left')



