"""
Hex Colour Lookup
Estimate: 12 min
Actual:   ___ min
"""

NAME_TO_HEX = {
    "aliceblue":      "#f0f8ff",
    "antiquewhite":   "#faebd7",
    "aquamarine":     "#7fffd4",
    "chartreuse":     "#7fff00",
    "cornflowerblue": "#6495ed",
    "darkorchid":     "#9932cc",
    "firebrick":      "#b22222",
    "goldenrod":      "#daa520",
    "indianred":      "#cd5c5c",
    "khaki":          "#f0e68c",
}


def main() -> None:
    """Lookup hexadecimal colour codes by name."""
    colour_name = input("Colour name: ").strip().lower()
    while colour_name:
        hex_code = NAME_TO_HEX.get(colour_name)
        if hex_code:
            print(f"{colour_name.title()} → {hex_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Colour name: ").strip().lower()


if __name__ == "__main__":
    main()
