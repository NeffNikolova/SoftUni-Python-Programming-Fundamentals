numbers_string = input().split(', ')
numbers_string = [int(number) for number in (numbers_string)]
print([index for index, num in enumerate(numbers_string) if num % 2 == 0])


