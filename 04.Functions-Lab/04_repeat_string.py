# def string_repeater(input_string:str, counter:int) -> str:
#     result = input_string * counter
#     return result
string_repeater = lambda input_string, counter: input_string * counter

current_string = input()
counter_value = int(input())

print(string_repeater(current_string, counter_value))
