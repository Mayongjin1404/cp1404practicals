"""
Word Occurrences
Estimate: 25 min
Actual:   ___ min
"""

from collections import Counter


def main() -> None:
    """Count and display how often each word appears in the input text."""
    text = input("Text: ").lower().split()
    counts = Counter(text)

    max_len = max(len(word) for word in counts)
    for word in sorted(counts):
        print(f"{word:{max_len}} : {counts[word]}")


if __name__ == "__main__":
    main()
