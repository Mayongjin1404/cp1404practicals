"""
score.py

Takes a score as input and classifies it.
Also demonstrates reusing function with random score.
"""

import random

def main():
    score = float(input("Enter score (0-100): "))
    print(determine_score_result(score))

    # Generate and evaluate a random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_score_result(random_score))

def determine_score_result(score):
    """Return the result string based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
