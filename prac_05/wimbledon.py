"""
Wimbledon Champions Data
Estimate: 30 min
Actual:   ___ min
"""

FILENAME = "wimbledon.csv"


def main() -> None:
    """Read data file, then display champions and winning countries."""
    years_data = get_data(FILENAME)
    champion_to_wins = count_wins(years_data)
    countries = extract_countries(years_data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items(), key=lambda item: item[1], reverse=True):
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def get_data(filename: str) -> list[list[str]]:
    """Return list of rows from CSV (year, country, champion)."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)               # skip header
        for line in in_file:
            year, country, champion = line.strip().split(",")
            data.append([year, country, champion])
    return data


def count_wins(data: list[list[str]]) -> dict[str, int]:
    """Return dict of champion → number of wins."""
    wins: dict[str, int] = {}
    for _, _, champion in data:
        wins[champion] = wins.get(champion, 0) + 1
    return wins


def extract_countries(data: list[list[str]]) -> set[str]:
    """Return a set of all countries in dataset."""
    return {country for _, country, _ in data}


if __name__ == "__main__":
    main()
