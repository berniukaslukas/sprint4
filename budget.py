import sqlite3


class Budget:
    def __init__(self, conn):
        self.conn = conn

    def set_budget(self, category, limit_amount):
        if limit_amount <= 0:
            print("Limit amount must be greater than 0.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT OR REPLACE INTO budgets (category, limit_amount) VALUES (?, ?)",
                (category.strip(), limit_amount),
            )
            self.conn.commit()
            print(f"Budget set for {category} with a limit of {limit_amount}.")
        except sqlite3.Error as e:
            print(f"Error setting budget: {e}")

    def view_budgets(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM budgets")
            budgets = cursor.fetchall()

            if not budgets:
                print("No budgets found.")
                return

            print("\nBudgets:")
            print("Category".ljust(30) + "Limit Amount")
            print("-" * 50) 

            for budget in budgets:
                print(f"{budget[0]:<30} {budget[1]:<10}")
            print("-" * 50)
        except sqlite3.Error as e:
            print(f"Error viewing budgets: {e}")
