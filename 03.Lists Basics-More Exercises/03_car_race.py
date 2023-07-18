sequence_of_numbers = input().split()
all_numbers = len(sequence_of_numbers)

left_numbers = sequence_of_numbers[:(((all_numbers)//2))]
right_numbers = sequence_of_numbers[(((all_numbers)//2)+1):]
right_numbers.reverse()

left_numbers = list(map(int, left_numbers))
right_numbers = list(map(int, right_numbers))

left_time = 0
right_time = 0

for number in left_numbers:
    if number != 0:
        left_time += number
    else:
        left_time *= 0.80

for number in right_numbers:
    if number != 0:
        right_time += number
    else:
        right_time *= 0.80

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")