key = int(input())
number_of_lines = int(input())

message = ''

for line in range(number_of_lines):
    letter = input()
    decrypted_letter = chr(ord(letter) + key)
    message += decrypted_letter

print(message)