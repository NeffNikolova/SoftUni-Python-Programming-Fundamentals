def fire(lst,ind,value):
    ind = int(ind)
    if 0 <= ind < len(lst):
        lst[ind] = int(lst[ind]) - int(value)
        if int(lst[ind]) <= 0:
            lst.pop(int(ind))
            print("You won! The enemy ship has sunken.")
            return True
    return False


def defend(lst,start,end,value):
    start = int(start)
    end = int(end)
    if 0 <= start < len(lst) and 0 <= end < len(lst):
        for ind in range(start, end + 1):
            lst[ind] = int(lst[ind]) - int(value)
            if int(lst[ind]) <= 0:
                lst.pop(int(ind))
                print(f"You lost! The pirate ship has sunken.")
                return True
    return False


def repair(lst, ind, value, max_health):
    ind = int(ind)
    if 0 <= ind < len(lst):
        if int(lst[ind]) + int(value) <= max_health:
            lst[ind] = int(lst[ind]) + int(value)
        else:
            lst[ind] = max_health
    return lst


def status(lst,max_health):
    for_repair = [value for value in lst if int(value) < max_health*0.20]
    print(f"{int(len(for_repair))} sections need repair.")
    return lst


pirate_ship_status = [int(el) for el in input().split('>')]
warship_status = [int(el) for el in input().split('>')]
maximum_health_capacity = int(input())
command = input()
stop = False
while command != 'Retire':
    if 'Fire' in command:
        action, index_to_fire_at, damage = command.split()
        stop = fire(warship_status, index_to_fire_at, damage)
        if stop:
            break
    elif 'Defend' in command:
        action, start_ind, end_ind, damage = command.split()
        stop = defend(pirate_ship_status, start_ind, end_ind, damage)
        if stop:
            break
    elif 'Repair' in command:
        action, index_to_repair, health = command.split()
        pirate_ship_status = repair(pirate_ship_status, index_to_repair,health, maximum_health_capacity)
    elif 'Status' in command:
        pirate_ship_status = status(pirate_ship_status, maximum_health_capacity)
    command = input()
else:
    print(f"Pirate ship status: {sum(pirate_ship_status)}\nWarship status: {sum(warship_status)}")
