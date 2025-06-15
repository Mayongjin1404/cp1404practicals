"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject data and display details."""
    data = load_data()
    display_subject_details(data)


def load_data():
    """
    Read data from file formatted like: subject,lecturer,number of students.
    Return a nested list: [[code, lecturer, students], ...]
    """
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # convert student number to int
            data.append(parts)
    return data


def display_subject_details(data):
    """Display subject details in the required format."""
    for subject, lecturer, students in data:
        print(f"{subject} is taught by {lecturer} and has {students:3} students")


if __name__ == "__main__":
    main()
