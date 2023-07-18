input_string = input()
letters = ''
digits = ''
other = ''

for ch in input_string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other += ch

print(digits)
print(letters)
print(other)