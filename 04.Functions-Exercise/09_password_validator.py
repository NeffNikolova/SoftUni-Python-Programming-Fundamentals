def pass_validator(some_password: str) -> bool:

    pass_valid = True

    if not 6 <= len(some_password) <= 10:
        print("Password must be between 6 and 10 characters")
        pass_valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        pass_valid = False

    digits_in_pass = 0
    for char in some_password:
        if char.isdigit():
            digits_in_pass += 1

    if digits_in_pass < 2:
        print("Password must have at least 2 digits")
        pass_valid = False

    return pass_valid


current_password = input()

if pass_validator(current_password):
    print("Password is valid")

