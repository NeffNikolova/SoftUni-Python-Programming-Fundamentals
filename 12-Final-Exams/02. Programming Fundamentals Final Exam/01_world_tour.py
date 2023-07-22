def add_stop(plan, command):
    action, index, string = command.split(':')
    if 0 <= int(index) < len(plan):
        left_side = plan[:int(index)]
        right_side = plan[int(index):]
        return left_side + string + right_side
    return None


def remove_stop(plan, command):
    action, start_index, end_index = command.split(':')
    if 0 <= int(start_index) < len(plan) and 0 <= int(end_index) < len(plan):
        left_side = plan[:int(start_index)]
        right_side = plan[int(end_index) + 1:]
        return left_side + right_side
    return None


def switch(plan, command):
    action, old_string, new_string = command.split(':')
    if old_string in plan:
        result = plan.replace(old_string, new_string)
        return result
    return None


travel_plan = input()
current_command = input()

while current_command != 'Travel':
    if 'Add Stop' in current_command:
        if add_stop(travel_plan, current_command):
            travel_plan = add_stop(travel_plan, current_command)
        print(travel_plan)
    elif 'Remove Stop' in current_command:
        if remove_stop(travel_plan, current_command):
            travel_plan = remove_stop(travel_plan, current_command)
        print(travel_plan)
    elif 'Switch' in current_command:
        if switch(travel_plan, current_command):
            travel_plan = switch(travel_plan, current_command)
        print(travel_plan)
    current_command = input()

print(f'Ready for world tour! Planned stops: {travel_plan}')