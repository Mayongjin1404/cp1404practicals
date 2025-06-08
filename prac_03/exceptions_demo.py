"""
exceptions_demo.py

Example to demonstrate exception handling and explanation.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("ValueError: Invalid input. You must enter an integer.")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
else:
    print(f"Result is {result}")
print("Finished.")

# 1. ValueError will occur when input cannot be converted to int (e.g., letters).
# 2. ZeroDivisionError will occur when denominator is 0.
# 3. To avoid ZeroDivisionError, we can check if denominator is 0 before division.
