"""
CP1404/CP5632 Practical
Quick Pick lottery ticket generator
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate a given number of quick-pick lottery tickets."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        # Format: each number right-aligned in 2 spaces
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a sorted quick-pick list of unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


if __name__ == "__main__":
    main()
