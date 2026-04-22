"""
Database Module for Price Tracker
Purpose: Initialize SQLite database and store cleaned price data
Data Source: data/cleaned_data.csv (from cleaning pipeline)

Database Schema:
- id: Unique identifier (auto-increment)
- name: Product name (TEXT)
- price: Product price (REAL/float)
- scraped_at: Timestamp of when data was inserted (TEXT)
"""

import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "data/products.db"

def init_db():
    """
    Initialize SQLite database with products table if it doesn't exist.
    
    Decision: Use SQLite (not PostgreSQL) for:
    - Simplicity: No server setup needed
    - Portability: Single file database
    - Development: Suitable for demo/prototype
    - Future: Easy to migrate to PostgreSQL if needed
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create table with schema
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
    """
    Read cleaned data from CSV and insert into database.
    
    Process:
    1. Read cleaned_data.csv using Pandas
    2. Iterate through each row
    3. Insert into products table with current timestamp
    4. Commit transaction
    
    Decision: Re-insert all data on each run
    Reason: Ensures database is always in sync with latest cleaned data
    """
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_csv("data/cleaned_data.csv")

    for _, row in df.iterrows():
        conn.execute(
            "INSERT INTO products (name, price, scraped_at) VALUES (?, ?, ?)",
            (row["name"], row["price"], datetime.now())
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    insert_data()