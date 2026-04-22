# API application
# TODO: Implement Flask/FastAPI app

import os
from dotenv import load_dotenv
from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

DB_NAME = os.getenv("DB_PATH", "data/products.db")

@app.get("/")
def home():
    return {"message": "Price Tracker API Running"}

@app.get("/products")
def get_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name, price, scraped_at FROM products")
    data = cursor.fetchall()

    conn.close()

    return {"data": data}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ NEW ENDPOINT
@app.get("/average-price")
def average_price():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(price) FROM products")
    avg_price = cursor.fetchone()[0]

    conn.close()

    return {
        "average_price": round(avg_price, 2) if avg_price else 0
    }