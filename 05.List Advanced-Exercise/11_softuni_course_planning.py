def swap_command(schedule, lesson1,lesson2, exercise_1, exercise_2):
    first_index = schedule.index(lesson1)
    second_index = schedule.index(lesson2)
    if lesson1 and lesson2 in schedule:
        exercise_1_index = schedule.index(exercise_1) if exercise_1 in schedule else None
        exercise_2_index = schedule.index(exercise_2) if exercise_2 in schedule else None
        schedule[first_index], schedule[second_index] = \
            schedule[second_index], schedule[first_index]
        if exercise_1 in schedule:
            schedule.pop(exercise_1_index)
            schedule.insert(second_index + 1, exercise1)
        if exercise_2 in schedule:
            schedule.pop(exercise_2_index)
            schedule.insert(first_index + 1, exercise2)
    return schedule


def exercise_command(lesson_, schedule,exercise_):
    if lesson_ in schedule:
        lesson_index = schedule.index(lesson_)
        schedule.insert(lesson_index + 1, exercise_)
    else:
        schedule.append(lesson_)
        schedule.append(exercise_)
    return schedule


initial_schedule = input().split(', ')
command = input()

while command != 'course start':
    command_list = command.split(':')

    if command_list[0] == 'Add':
        initial_schedule.append(command_list[1]) if command_list[1] not in initial_schedule else initial_schedule
    elif command_list[0] == 'Insert':
        lesson = command_list[1]
        index = int(command_list[2])
        initial_schedule.insert(index, lesson) if lesson not in initial_schedule else initial_schedule
    elif command_list[0] == 'Remove':
        initial_schedule.remove(command_list[1]) if command_list[1] in initial_schedule else initial_schedule
        exercise = command_list[1] + '-Exercise'
        initial_schedule.remove(command_list[1]) if exercise in initial_schedule else initial_schedule
    elif command_list[0] == 'Swap':
        exercise1 = command_list[1] + '-Exercise'
        exercise2 = command_list[2] + '-Exercise'
        swap_command(initial_schedule, command_list[1], command_list[2], exercise1, exercise2)
    elif command_list[0] == 'Exercise':
        lesson = command_list[1]
        exercise = lesson + '-Exercise'
        exercise_command(lesson, initial_schedule, exercise)

    command = input()

num = 1
for el in initial_schedule:
    print(f'{num}.{el}')
    num += 1
