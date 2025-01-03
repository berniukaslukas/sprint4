from handlers import Handlers
from menu import Menu
from database import Database
import sqlite3


def main():
    db = Database("personal_finance.db")
    conn = db.initialize()

    if not conn:
        print("Failed to initialize the database. Exiting.")
        return

    handlers = Handlers(conn)

    menu = Menu(handlers)

    menu.run()

    conn.close()


if __name__ == "__main__":
    main()
