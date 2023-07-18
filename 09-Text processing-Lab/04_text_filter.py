banned_words = input().split(', ')
text_to_edit = input()

for word in banned_words:
    text_to_edit = text_to_edit.replace(word, '*' * len(word))
print(text_to_edit)