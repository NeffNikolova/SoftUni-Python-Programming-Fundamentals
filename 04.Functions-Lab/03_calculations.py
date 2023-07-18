def calculator(operator:str,value1:int,value2:int) -> int:
    result = 0
    if operator == "multiply":
        result = value1 * value2
    elif operator == 'divide':
        result = int(value1 / value2)
    elif operator == 'add':
        result = value1 + value2
    elif operator == 'subtract':
        result = value1 - value2
    return result


current_operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(current_operator, first_number, second_number))
