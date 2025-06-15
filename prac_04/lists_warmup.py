"""
CP1404/CP5632 Practical
Lists warm‑up exercises
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted answers (without running the code):
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Actual answers (run to verify)
# Uncomment the following lines to check
# print(numbers[0])
# print(numbers[-1])
# print(numbers[3])
# print(numbers[:-1])
# print(numbers[3:4])
# print(5 in numbers)
# print(7 in numbers)
# print("3" in numbers)
# print(numbers + [6, 5, 3])

# 1. Change the first element to "ten"
numbers[0] = "ten"

# 2. Change the last element to 1
numbers[-1] = 1

# 3. Print all elements except the first two
print("Numbers except the first two:", numbers[2:])

# 4. Print whether 9 is an element of numbers
print("Does the list contain 9?", 9 in numbers)
