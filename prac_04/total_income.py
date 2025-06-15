"""
CP1404/CP5632 Practical
Refactored cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes)


def print_report(incomes):
    """Print a formatted income report from a list of incomes."""
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${total:10.2f}")


if __name__ == "__main__":
    main()
