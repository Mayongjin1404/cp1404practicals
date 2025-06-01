def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print("\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print("*" * score)
        elif choice == "Q":
            print("Farewell.")
        else:
            print("Invalid choice")

main()