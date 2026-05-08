MICROSCOPES = {
    1: ("Light Microscope", 40),
    2: ("Compound Microscope", 100),
    3: ("Electron Microscope", 100000),
    4: ("Scanning Electron Microscope", 50000)
}

UNIT_CONVERSION = {
    "nm": 1e6,
    "µm": 1e3,
    "mm": 1,
    "cm": 0.1,
    "m": 0.001
}

def main():
    print("=== Microscope Calculator ===")

    measured = float(input("Enter measured size (mm): "))

    print("\nSelect Microscope:")
    for k, v in MICROSCOPES.items():
        print(f"{k}. {v[0]} ({v[1]}x)")

    choice = int(input("Choice: "))
    name, mag = MICROSCOPES[choice]

    print("\nSelect Unit:")
    units = list(UNIT_CONVERSION.keys())
    for i, u in enumerate(units, 1):
        print(f"{i}. {u}")

    u_choice = int(input("Choice: "))
    unit = units[u_choice - 1]

    real_mm = measured / mag
    converted = real_mm * UNIT_CONVERSION[unit]

    print("\n=== RESULT ===")
    print(f"{measured} ÷ {mag} = {real_mm} mm")
    print(f"Converted: {converted} {unit}")

main()