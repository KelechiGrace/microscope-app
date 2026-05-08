from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
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

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        username = request.form["username"]
        size = float(request.form["size"])
        microscope = request.form["microscope"]
        unit = request.form["unit"]

        mag = MICROSCOPES[microscope]
        real = size / mag
        converted = real * UNIT_CONVERSION[unit]

        insert_record(username, size, real)
        result = f"{converted} {unit}"

    return render_template("index.html",
                           microscopes=MICROSCOPES.keys(),
                           units=UNIT_CONVERSION.keys(),
                           result=result)

@app.route("/records")
def records():
    data = get_records()
    return render_template("records.html", records=data)

if __name__ == "__main__":
    app.run(debug=True)