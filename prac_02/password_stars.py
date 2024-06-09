# password_stars.py

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def is_valid_password(password):
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        pass
    return True

main()
