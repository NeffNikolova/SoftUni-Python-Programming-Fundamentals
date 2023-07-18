first_row = input().split()
second_row = input().split()
third_row = input().split()

winner = False
winner_nr = 0
if first_row[0] == second_row[0] == third_row[0] != '0':
    winner = True
    winner_nr = first_row[0]
elif first_row[1] == second_row[1] == third_row[1] != '0':
    winner = True
    winner_nr = first_row[1]
elif first_row[2] == second_row[2] == third_row[2] != '0':
    winner = True
    winner_nr = first_row[2]
elif first_row[0] == second_row[1] == third_row[2] != '0':
    winner = True
    winner_nr = first_row[0]
elif first_row[2] == second_row[1] == third_row[0] != '0':
    winner = True
    winner_nr = first_row[2]
elif first_row[0] == first_row[1] == first_row[2] != '0':
    winner = True
    winner_nr = first_row[2]
elif second_row[0] == second_row[1] == second_row[2] != '0':
    winner = True
    winner_nr = second_row[2]
elif third_row[0] == third_row[1] == third_row[2] != '0':
    winner = True
    winner_nr = third_row[2]
else:
    winner = False

if winner:
    if winner_nr == '1':
        print('First player won')
    if winner_nr == '2':
        print('Second player won')
else:
    print('Draw!')
