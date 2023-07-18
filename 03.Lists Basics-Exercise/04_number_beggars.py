amounts = input()
beggars_nr = int(input())

list_amounts = amounts.split(', ')
current_beggar_sum = []
all_beggars_sums = []
for beggar in range(1, beggars_nr+1):
    for amount in range(beggar - 1, len(list_amounts),beggars_nr):
        current_beggar_sum.append(int(list_amounts[amount]))

    all_beggars_sums.append(sum(current_beggar_sum))
    current_beggar_sum.clear()
print(all_beggars_sums)