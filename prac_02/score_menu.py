"""
score_menu.py

Menu-driven program to interact with user scores.
"""

def main():
    score = get_valid_score()
    choice = display_menu()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = display_menu()

    print("Goodbye!")

def display_menu():
    """Show the menu and return the user's choice"""
    print("
Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    return input(">>> ").upper()

def get_valid_score():
    """Prompt user for a valid score between 0 and 100"""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score

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
