
string_input = input()
# bring input to lowercase as results should not be case sensitive
string_input = string_input.lower()
my_list = ['sand', 'water', 'fish', 'sun']
matches = 0
# for each element in list
for i in my_list:
    # check number of times to appear in string
    string_input.count(i)
    # keep number of matches into matches variable by adding the found ones each iteration
    matches += int(string_input.count(i))
print(matches)
