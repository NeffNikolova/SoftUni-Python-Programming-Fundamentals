from math import factorial


def factorial_dividion(num1:int, num2:int) -> float:
    return factorial(num1) / factorial(num2)


first_number = int(input())
second_number = int(input())

print(f'{factorial_dividion(first_number, second_number):.2f}')
