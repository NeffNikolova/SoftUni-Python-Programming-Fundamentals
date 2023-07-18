input_text = input().split()
output_text = [word for word in input_text if len(word) % 2 == 0]
print(*output_text, sep='\n')