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
        FROM products p
        """)
        products = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            product = Product(row['id'], row['name'], row['price'])
            products.append(product.__dict__)
    return products
def get_single_product(id):
    """sql get single products"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM products p
        WHERE p.id = ?
        """, (id, ))
    data = db_cursor.fetchone()
    product = Product(data['id'], data['name'], data['price'])

    return product.__dict__
def create_product(new_product):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Products
            ( name, price)
        VALUES 
            ( ?, ?);
        """, (new_product['name'], new_product['price']))

        id = db_cursor.lastrowid
        new_product['id'] = id
    return new_product

def update_product(id, product):
     with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Products 
            SET
                name = ?,
                price = ?
        WHERE id = ?
        """, (product['name'], product['price'], id))
        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        
        return True
