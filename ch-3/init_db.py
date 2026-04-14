import sqlite3
import os
import sys

conn = sqlite3.connect("SalesDB/sales.db")

cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)
''')

cursor.execute('''
               INSERT INTO sales (product_name, quantity, price, sale_date) VALUES
               ('Laptop', 2, 1200.00, '2024-01-15'),
               ('Smartphone', 5, 800.00, '2024-01-20'),
               ('Headphones', 10, 150.00, '2024-01-25'),
               ('Monitor', 3, 300.00, '2024-01-30'),
               ('Keyboard', 7, 100.00, '2024-02-05  ')
''')

conn.commit()
conn.close()