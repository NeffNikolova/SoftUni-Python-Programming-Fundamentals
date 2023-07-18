number_of_strings = int(input())
keyword = input()

all_words_list = []
filtered_list = []
for number in range(number_of_strings):
    current_string = input()
    all_words_list.append(current_string)
    if keyword in current_string:
        filtered_list.append(current_string)

print(all_words_list)
print(filtered_list)
