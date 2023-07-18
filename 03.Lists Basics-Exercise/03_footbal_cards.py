team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input()
terminated = False

for card in cards.split():
    current_team = card.split('-')[0]
    current_player = card.split('-')[1]
    if current_team == 'A':
        if int(current_player) in team_A:
            team_A.remove(int(current_player))
    elif current_team == 'B':
        if int(current_player) in team_B:
            team_B.remove(int(current_player))

    if len(team_A) < 7 or len(team_B) < 7:
        terminated = True
        break

print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')

if terminated:
    print('Game was terminated')