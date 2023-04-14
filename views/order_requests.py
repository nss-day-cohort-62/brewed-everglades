import sqlite3
import json
from models import Order


def get_all_orders():
    """sql get all products"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.product_id,
            o.employee_id,
            o.timestamp
        FROM orders o
        """)
        orders = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            order = Order(row['id'], row['product_id'],
                          row['employee_id'], row['timestamp'])
            orders.append(order.__dict__)
    return orders


def get_single_order(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.product_id,
            o.employee_id,
            o.timestamp
        FROM orders o
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['product_id'],
                      data['employee_id'], data['timestamp'])

        return order.__dict__


def create_order(new_order):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Orders 
            (product_id, employee_id, timestamp)
        VALUES
            (?, ?, ?);
        """, (new_order['product_id'], new_order['employee_id'], new_order['timestamp'], ))
        id = db_cursor.lastrowid
        new_order['id'] = id
    return new_order


def update_order(id, updated_order):
    """function for updating orders"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Orders
            SET
                product_id = ?,
                employee_id = ?,
                timestamp = ?
            WHERE id = ?
            """, (updated_order['product_id'], updated_order['employee_id'], updated_order['timestamp'], id, ))
        rows_affected = db_cursor.rowcount
        if rows_affected == 0:
            return False
        return True
