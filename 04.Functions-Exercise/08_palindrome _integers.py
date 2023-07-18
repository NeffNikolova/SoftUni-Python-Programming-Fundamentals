def test_palindrome(some_list:list):
    current_list = []
    reversed_list = []
    is_palindrome_list = []
    for number in some_list:
        for num in str(number):
            current_list.append(num)
        reversed_list.extend(current_list)
        reversed_list.reverse()

        if reversed_list == current_list:
            current_list.clear()
            reversed_list.clear()
            is_palindrome_list.append('True')
        else:
            current_list.clear()
            reversed_list.clear()
            is_palindrome_list.append('False')

    return is_palindrome_list


list_of_integers = input().split(', ')
# list_of_integers = list(map(int, list_of_integers))

print('\n'.join(test_palindrome(list_of_integers)))


