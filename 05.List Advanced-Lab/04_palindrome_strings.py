from audioop import reverse

sequence = input().split()
target_palindrome = input()
# palindromes = []
palindromes = [word for word in sequence if word == ''.join(reversed(word))]
# for word in sequence:
#     if word in sequence == reversed(word):
#         palindromes.append(word)

number_target_in_list = [1 for word in palindromes if word == target_palindrome]

print(palindromes)
print(f'Found palindrome {sum(number_target_in_list)} times')
