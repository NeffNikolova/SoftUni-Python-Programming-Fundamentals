import re

barcodes_count = int(input())
current_group = ''

for entry in range(barcodes_count):
    barcode_entry = input()
    pattern = r"^@[#]+([A-Z][A-Za-z0-9]{4,}[A-Z])@[#]+$"
    match = re.fullmatch(pattern, barcode_entry)
    if match:
        for index in range(len(match.group(1))):
            if match.group(1)[index].isdigit():
                current_group += match.group(1)[index]
        if current_group == '':
            current_group = '00'
        print(f'Product group: {current_group}')
        current_group = str('')
    else:
        print('Invalid barcode')



