from database import *
create_table()

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

username = input("Enter username: ")
measured = float(input("Measured size (mm): "))

print("Select microscope:")
for k, v in MICROSCOPES.items():
    print(f"{k}. {v[0]}")

choice = int(input("Choice: "))
name, mag = MICROSCOPES[choice]

real = measured / mag

insert_record(username, measured, real)

print("Saved!")
print("\nRecords:")
for r in get_records():
    print(r)