import sqlite3

DB_PATH = "app.db"

def get_connection():
    """Creates and returns database connection"""
    return sqlite3.connect(DB_PATH)

def get_user_by_id(user_id):
    """Fetches user from database by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def create_user(username, email):
    """Creates a new user in database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (username, email)
    )
    conn.commit()
    return cursor.lastrowid

def delete_user(user_id):
    """Deletes user from database by ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
