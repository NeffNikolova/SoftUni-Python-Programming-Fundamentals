items = input().split()
searched_items = input().split()
stock = {}

for index in range(0, len(items), 2):
    stock[items[index]] = int(items[index+1])

for item in searched_items:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
