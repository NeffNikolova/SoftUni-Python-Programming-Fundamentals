first_string, second_string = input().split()
total_sum_chars = 0
uneven = False

if len(first_string) != len(second_string):
    diff = abs(len(first_string) - len(second_string))
    max_len_multiply = int(((len(first_string) + len(second_string)) - diff)/2)
    uneven = True
else:
    max_len_multiply = len(first_string)

for i in range(0, max_len_multiply):
    total_sum_chars += ord(first_string[i])*ord(second_string[i])

if uneven:
    if len(first_string) > len(second_string):
        for i in range(max_len_multiply, len(first_string)):
            total_sum_chars += ord(first_string[i])
    else:
        for i in range(max_len_multiply, len(second_string)):
            total_sum_chars += ord(second_string[i])
print(total_sum_chars)