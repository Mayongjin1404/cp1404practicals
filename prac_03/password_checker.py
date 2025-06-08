"""
password_checker.py

Validates a password based on several conditions.
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\"

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("	1 or more uppercase characters")
    print("	1 or more lowercase characters")
    print("	1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"	and 1 or more special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = count_upper = count_digit = count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower and count_upper and count_digit:
        if SPECIAL_CHARS_REQUIRED:
            return count_special > 0
        return True
    return False

main()
