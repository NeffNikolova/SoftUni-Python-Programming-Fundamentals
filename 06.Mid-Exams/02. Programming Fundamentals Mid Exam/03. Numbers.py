sequence = input().split()
length = len(sequence)
sequence = [int(element) for element in sequence]

average = sum(sequence)/length

greater_avg_nr = [el for el in sequence if el > average]
greater_avg_nr.sort(reverse=True)
for element in greater_avg_nr[::-1]:
    if greater_avg_nr.index(element) > 4:
        greater_avg_nr.pop(greater_avg_nr.index(element))

if not greater_avg_nr:
    print('No')
else:
    print(*greater_avg_nr, sep=' ')