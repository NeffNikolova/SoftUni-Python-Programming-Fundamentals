first_sequence = input().split(', ')
second_sequence = input().split(', ')
matching_words = list()

for word in first_sequence:
    for text in second_sequence:
        if word in text and word not in matching_words:
            matching_words.append(word)
    # [word for word in first_sequence if word in text and
        #                    word not in matching_words]
# matching_words = list(set(matching_words))
print(matching_words)

