number_of_snowballs = int(input())

highest_value = 0
highest_time = 0
highest_weight = 0
highest_quality = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())

    snowball_value = (weight / time_to_target) ** quality

    if snowball_value > highest_value:
        highest_value = int(snowball_value)
        highest_time = int(time_to_target)
        highest_weight = int(weight)
        highest_quality = int(quality)

print(f'{highest_weight} : {highest_time} = {highest_value} ({highest_quality})')