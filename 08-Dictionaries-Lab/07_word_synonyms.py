number_of_words = int(input())
synonyms = {}

for i in range(number_of_words):
    key_word = input()
    synonym_word = input()
    if key_word not in synonyms:
        synonyms[key_word] = []
    synonyms[key_word].append(synonym_word)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}", end ='\n')

