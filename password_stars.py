def get_password(min_length=6):
    password = input("Enter a password: ")
    while len(password) < min_length:
        print("Password too short.")
        password = input("Enter a password: ")
    return password

def print_stars(password):
    print("*" * len(password))

def main():
    password = get_password()
    print_stars(password)

main()