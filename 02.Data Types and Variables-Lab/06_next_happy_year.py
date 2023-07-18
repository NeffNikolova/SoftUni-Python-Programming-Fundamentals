given_year = int(input())

while True:
    given_year += 1
    given_year_str = str(given_year)
    # convert the character in the given_year_str string into entries in a set.
    # Set can only contain unique values
    # Compare the number of entries in the set to the number of characters in the year
    # and only print if both equal, as this would mean all chars are unique
    if len(set(given_year_str)) == len(given_year_str):
        break
print(given_year)
