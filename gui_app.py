import tkinter as tk
from tkinter import ttk, filedialog
from database import *

create_table()

MICROSCOPES = {
    "Light Microscope": 40,
    "Compound Microscope": 100,
    "Electron Microscope": 100000,
    "SEM": 50000
}

UNIT_CONVERSION = {
    "nm": 1e6,
    "µm": 1e3,
    "mm": 1,
    "cm": 0.1,
    "m": 0.001
}

def upload():
    filedialog.askopenfilename()

def calculate():
    username = user_entry.get()
    size = float(size_entry.get())
    mag = MICROSCOPES[micro_var.get()]
    unit = unit_var.get()

    real = size / mag
    converted = real * UNIT_CONVERSION[unit]

    result.config(text=f"{converted} {unit}")

    insert_record(username, size, real)

root = tk.Tk()
root.title("Microscope GUI")

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Size (mm)").pack()
size_entry = tk.Entry(root)
size_entry.pack()

micro_var = tk.StringVar()
ttk.Combobox(root, textvariable=micro_var,
             values=list(MICROSCOPES.keys())).pack()

unit_var = tk.StringVar()
ttk.Combobox(root, textvariable=unit_var,
             values=list(UNIT_CONVERSION.keys())).pack()

tk.Button(root, text="Upload Image", command=upload).pack()
tk.Button(root, text="Calculate", command=calculate).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()