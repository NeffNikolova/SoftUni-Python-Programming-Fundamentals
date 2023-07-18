list_input = input()
# text to column - convert input to list with defined separator
user_list = list_input.split(', ')
# reverse list order
user_list.reverse()
# define sheep Nr
N = 0
# for each element in the list
for i in user_list:
    # if wolf is first
    if user_list.index(i) == 0 and i == 'wolf':
        print("Please go away and stop eating my sheep")
        break
    # if wolf is not first
    elif user_list.index(i) != 0 and i == 'wolf':
        # get position of sheep = the next from current element position, but wolf does not count, so position equals
        # wolf position = current position
        N = user_list.index(i)
        print(f"Oi! Sheep number {N}! You are about to be eaten by a wolf!")
        break
