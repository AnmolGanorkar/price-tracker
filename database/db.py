# Database module
# TODO: Implement database connection and operations

import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "data/products.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        scraped_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_csv("data/cleaned_data.csv")

    for _, row in df.iterrows():
        conn.execute(
            "INSERT INTO products (name, price, scraped_at) VALUES (?, ?, ?)",
            (row["name"], row["price"], datetime.now())
        )

    conn.commit()
    conn.close()

if __name__ != "__main__":
    init_db()
    insert_data()