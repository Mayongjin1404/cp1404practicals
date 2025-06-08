"""
string_formatting.py

Practice with string formatting using f-strings.
"""

# Display guitar details using string formatting
name = "Gibson L-5 CES"
year = 1922
cost = 16035.0
print(f"{year} {name} for about ${cost:,.0f}!")

# Print powers of 2 using formatting
for i in range(0, 11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
