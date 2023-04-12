import sqlite3
import json
from models import Product

def get_all_products():
    """sql get all products"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM product p
        """)
        products = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            product = Product(row['id'], row['name'], row['price'])
            products.append(product.__dict__)
    return products
