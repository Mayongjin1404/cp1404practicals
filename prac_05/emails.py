"""
Emails & Names Dictionary
Estimate: 20 min
Actual:   ___ min
"""

def extract_name(email: str) -> str:
    """Derive a likely name from an email address."""
    local_part = email.split("@")[0]
    parts = local_part.replace(".", " ").split()
    return " ".join(parts).title()


def main() -> None:
    """Build a dict of {email: name} with optional confirmation."""
    email_to_name: dict[str, str] = {}

    email = input("Email: ").strip()
    while email:
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
