countries = input().split(', ')
capitals = input().split(', ')

couples = {}

for index, value in enumerate(countries):
    couples[value] = capitals[index]

for key, value in couples.items():
    print(f'{key} -> {value}')
