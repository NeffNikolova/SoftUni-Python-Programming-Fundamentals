numbers_list = input().split()
string_input = input()
# numbers_list = list(map(int, numbers_list))
current_sum = 0
alt_current_sum = 0
message = ''

for current_element in numbers_list:
    for i in range(len(current_element)):
        current_sum += int(current_element[i])
    if current_sum >= len(string_input):
        alt_current_sum = current_sum % len(string_input)
        message += string_input[alt_current_sum]
        string_input = string_input[:alt_current_sum] + string_input[alt_current_sum+1:]
    else:
        message += string_input[current_sum]
        string_input = string_input[:current_sum] + string_input[current_sum + 1:]
    current_sum = 0
    alt_current_sum = 0

print(message)