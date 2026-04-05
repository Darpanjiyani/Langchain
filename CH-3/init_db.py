import sqlite3
from sqlalchemy.dialects import sqlite
import os
import sys

conn = sqlite3.connect("SalesDB/sales.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    price REAL
)
""")

orders = [
    ("Alice", "Laptop", 1, 1200.00),
    ("Bob", "Mouse", 2, 25.00),
    ("Charlie", "Keyboard", 1, 75.00),
    ("Alice", "Monitor", 1, 300.00),
    ("David", "Laptop", 1, 1200.00),
    ("Bob", "Webcam", 1, 50.00),
    ("Alice", "Docking Station", 1, 150.00),
    ("Charlie", "Monitor", 2, 300.00),
    ("David", "Keyboard", 1, 75.00),
    ("Eve", "Laptop", 1, 1200.00),
    ("Alice", "USB Hub", 3, 20.00),
    ("Bob", "Laptop", 1, 1200.00),
    ("Charlie", "Mouse", 1, 25.00),
    ("David", "Monitor", 1, 300.00),
    ("Eve", "Keyboard", 1, 75.00),
    ("Alice", "Laptop", 1, 1200.00),
    ("Bob", "Monitor", 1, 300.00),
    ("Charlie", "Webcam", 1, 50.00),
    ("David", "Docking Station", 1, 150.00),
    ("Eve", "Mouse", 2, 25.00)
]

cursor.executemany("""
INSERT INTO orders (customer_name, product_name, quantity, price)
VALUES (?, ?, ?, ?)
""", orders)

conn.commit()
conn.close()

print("Database initialized successfully!") 