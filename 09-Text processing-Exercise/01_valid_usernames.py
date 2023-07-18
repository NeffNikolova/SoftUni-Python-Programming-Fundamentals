usernames = input().split(', ')
approved_usernames = []

approved = False

for username in usernames:
    if 3 <= len(username) <= 16:
        for ch in username:
            if ch.isalnum() or ch == '-' or ch == '_':
                approved = True
            else:
                approved = False
                break
        if approved:
            approved_usernames.append(username)
        approved = False

print(*approved_usernames, sep='\n')
