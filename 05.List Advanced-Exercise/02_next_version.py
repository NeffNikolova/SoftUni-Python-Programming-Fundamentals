current_version = input().split('.')
current_num = int(''.join(current_version))
next_num = current_num + 1
next_version = []
next_version += [str(next_num)[0]] + [str(next_num)[1]] + [str(next_num)[2]]
print('.'.join(next_version))