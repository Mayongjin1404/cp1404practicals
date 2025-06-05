"""
password_stars.py

Prompts the user for a password and prints asterisks (*) equal to its length.
Uses functions for modularity.
"""

def main():
    password = get_password()
    print_stars(password)

def get_password():
    """Get a valid password from the user"""
    MIN_LENGTH = 6
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password

def print_stars(password):
    """Print asterisks equal to the length of the password"""
    print("*" * len(password))

main()
