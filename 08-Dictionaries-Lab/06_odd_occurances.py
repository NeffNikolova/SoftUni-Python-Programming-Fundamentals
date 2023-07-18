sequence_of_words = [element.lower() for element in input().split()]
number_of_words = {}

for element in sequence_of_words:
    if element not in number_of_words:
        number_of_words[element] = 0
    number_of_words[element] += 1

for key, value in number_of_words.items():
    if value % 2 != 0:
        print(key, end=' ')
