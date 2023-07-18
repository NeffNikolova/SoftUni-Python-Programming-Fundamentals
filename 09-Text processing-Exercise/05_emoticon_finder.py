input_text = input()
starting_index = 0
output = []
for i in range(len(input_text)):
    if input_text[i] == ':' and not input_text[i+1].isspace():
        output.append(input_text[i]+input_text[i+1])
print(*output, sep='\n')
