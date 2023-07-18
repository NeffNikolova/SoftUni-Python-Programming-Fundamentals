sequence_of_strings = input().split()

for string in sequence_of_strings:
    length = len(string)
    output = string * length
    print(output, end='')