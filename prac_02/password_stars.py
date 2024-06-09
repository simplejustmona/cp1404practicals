MIN_LENGTH = 8
def get_password():
    while True:
        password = input("Enter a password: ")
        if len(password) < MIN_LENGTH:
            print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")
        else:
            return password
password = get_password()
print('*' * len(password))
