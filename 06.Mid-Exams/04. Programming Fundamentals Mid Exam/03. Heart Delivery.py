def valentines(some_list, value):
    if int(some_list[value]) != 0:
        some_list[value] = str(int(some_list[value]) - 2)
        if int(some_list[value]) <= 0:
            some_list[value] = '0'
            print(f"Place {value} has Valentine's day.")
    else:
        print(f"Place {value} already had Valentine's day.")

    return some_list


neighbourhood = input().split('@')
command = input()
last_pos = 0
jump_value = 0

while command != 'Love!':
    jump_value = int(command.split()[1])
    if last_pos + jump_value >= len(neighbourhood):
        jump_value = 0
    else:
        jump_value = last_pos + jump_value
    neighbourhood = valentines(neighbourhood, jump_value)
    last_pos = jump_value
    command = input()

print(f"Cupid's last position was {jump_value}.")

neighbourhood = [int(element) for element in neighbourhood]
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    count_failed = [str(el) for el in neighbourhood if el != 0]
    print(f"Cupid has failed {len(count_failed)} places.")
