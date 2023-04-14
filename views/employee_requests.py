import sqlite3
from models import Employee


def get_all_employees():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.email,
            a.hourly_rate
        FROM employees a
        """)
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['email'], row['hourly_rate'])
            employees.append(employee.__dict__)
    return employees


def get_single_employee(id):
    """Method docstring."""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.email,
            a.hourly_rate
        FROM employees a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'],
                            data['email'], data['hourly_rate'])

        return employee.__dict__


def create_employee(new_employee):
    """Method docstring."""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO employees
            ( name, email, hourly_rate )
        VALUES
            ( ?, ?, ? );
        """, (new_employee['name'], new_employee['email'], new_employee['hourly_rate'], ))

        id = db_cursor.lastrowid

        new_employee['id'] = id

    return new_employee


def update_employee(id, new_employee):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employees
            SET
                name = ?,
                email = ?,
                hourly_rate = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['email'], new_employee['hourly_rate'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False

    return True
