"""
CP1404/CP5632 Practical 05
State names lookup and listing

- Re-formatted dictionary to PEP 8.
- Accepts lowercase inputs.
- Prints a neatly aligned list of all states on request.
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT":  "Northern Territory",
    "WA":  "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA":  "South Australia",
}


def main() -> None:
    """Run the state abbreviation lookup program."""
    print("Enter short state code to lookup; press Enter to list all and quit.")
    state_code = input("State code: ").strip().upper()

    while state_code:
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("State code: ").strip().upper()

    # Neatly print all states when loop ends
    print("\nAll states:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code:3} : {name}")


if __name__ == "__main__":
    main()
