# You will be receiving lines in the following format:
# "{username}-{language}-{points}" until you receive "exam finished".

# You should store each username and their submissions and points.
# if student has more submissions for same language, save only maximum points

# ban command - "{username}-banned".remove the user from the contest but preserve
# his submissions in the total count of submissions for each language.

# After receiving "exam finished", print each of the participants

command = input().split('-')
submissions = {}
all_points = {}

while command[0] != 'exam finished':
    if len(command) == 3:
        name, language, points = command[0], command[1], command[2]
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        if name in all_points.keys() and int(points) < int(all_points[name]):
            pass
        else:
            all_points[name] = int(points)
    elif len(command) == 2:
        user = command[0]
        for name in list(all_points.keys()):
            if name == user:
                del all_points[name]
    command = input().split('-')

print('Results:')
for key, value in all_points.items():
    print(f'{key} | {value}')
print('Submissions:')
for key, value in submissions.items():
    print(f'{key} - {value}')
