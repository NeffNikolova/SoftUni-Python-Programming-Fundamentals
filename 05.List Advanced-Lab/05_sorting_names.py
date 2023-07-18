names_list = input().split(', ')

names_list.sort(key=lambda x: (-len(x), x))
print(names_list)
