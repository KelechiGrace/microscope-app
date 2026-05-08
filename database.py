import sqlite3

def connect():
    return sqlite3.connect("microscope.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        measured REAL,
        real REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_record(username, measured, real):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO records (username, measured, real) VALUES (?, ?, ?)",
        (username, measured, real)
    )

    conn.commit()
    conn.close()

def get_records():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()

    conn.close()
    return rows