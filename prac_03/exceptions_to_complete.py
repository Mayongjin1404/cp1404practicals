"""
exceptions_to_complete.py

Handle invalid user input when converting to an integer.
"""

finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter an integer: "))
        result = number * 2
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Result is {result}")
