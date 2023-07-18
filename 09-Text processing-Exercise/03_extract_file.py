full_file_name = input().split("\\")[::-1]
file_name, file_ext = full_file_name[0].split('.')
print(f'File name: {file_name}\nFile extension: {file_ext}')