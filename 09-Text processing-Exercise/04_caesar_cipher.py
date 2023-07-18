text = input()
output = ''
for ch in text:
    new_ch = chr(ord(ch) + 3)
    output += new_ch

print(output)
