import sqlite3


class Database:
    def __init__(self, db_name="finance_tracker.db"):
        self.db_name = db_name

    def initialize(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS incomes (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              amount REAL NOT NULL,
                              category TEXT NOT NULL,
                              description TEXT,
                              date TEXT NOT NULL
                          )"""
            )

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS expenses (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              amount REAL NOT NULL,
                              category TEXT NOT NULL,
                              description TEXT,
                              date TEXT NOT NULL
                          )"""
            )

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS budgets (
                              category TEXT PRIMARY KEY,
                              limit_amount REAL NOT NULL
                          )"""
            )

            conn.commit()
            return conn
        except sqlite3.Error as e:
            print(f"Error initializing the database: {e}")
            return None
