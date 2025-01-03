import sqlite3
import datetime
import textwrap


class Record:
    def __init__(self, conn):
        self.conn = conn

    def add_record(self, table, amount, category, description, date=None):
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if not category.strip():
            print("Category cannot be blank.")
            return

        if len(description) > 255:
            description = description[:255]
            print("Description too long. It has been truncated.")

        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"INSERT INTO {table} (amount, category, description, date) VALUES (?, ?, ?, ?)",
                (amount, category.strip(), description.strip(), date),
            )
            self.conn.commit()
            print(f"Record added to {table}.")
        except sqlite3.Error as e:
            print(f"Error adding record: {e}")

    def view_records(self, table):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            records = cursor.fetchall()

            if not records:
                print(f"No records found in {table}.")
                return
            headers = ["ID", "Amount", "Category", "Description", "Date"]
            col_widths = [
                max(len(str(item)) for item in column)
                for column in zip(*records, headers)
            ]
            col_widths = [
                max(len(header), width) for header, width in zip(headers, col_widths)
            ]

            header_row = " | ".join(
                f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)
            )
            print(header_row)
            print("-" * len(header_row))

            for record in records:
                wrapped_description = "\n".join(
                    textwrap.wrap(record[3], width=col_widths[3])
                )  # Wrap description
                formatted_record = [
                    f"{record[0]:<{col_widths[0]}}",
                    f"{record[1]:<{col_widths[1]}}",
                    f"{record[2]:<{col_widths[2]}}",
                    wrapped_description,
                    f"{record[4]:<{col_widths[4]}}",
                ]
                print(" | ".join(formatted_record))
            print("-" * len(header_row))
        except sqlite3.Error as e:
            print(f"Error viewing records: {e}")

    def clear_database(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM incomes")
            cursor.execute("DELETE FROM expenses")
            cursor.execute("DELETE FROM budgets")
            self.conn.commit()
            print("All data has been cleared from the database.")
        except sqlite3.Error as e:
            print(f"Error clearing database: {e}")

    def clear_last_entry(self, table):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT id FROM {table} ORDER BY id DESC LIMIT 1")
            last_entry = cursor.fetchone()

            if last_entry:
                cursor.execute(f"DELETE FROM {table} WHERE id = ?", (last_entry[0],))
                self.conn.commit()
                print(f"Last entry has been removed from {table}.")
            else:
                print(f"No records found in {table}.")
        except sqlite3.Error as e:
            print(f"Error clearing last entry: {e}")
