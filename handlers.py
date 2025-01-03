from records import Record
from budget import Budget
from visualization import Visualization


class Handlers:
    def __init__(self, conn):
        self.conn = conn
        self.record_handler = Record(conn)
        self.budget_handler = Budget(conn)
        self.visualization_handler = Visualization(conn)

    def visualize_spending(self):
        self.visualization_handler.visualize_spending()

    def add_income(self):
        while True:
            try:
                amount = float(input("Enter income amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
        category = input("Enter income category: ")
        description = input("Enter description: ")
        self.record_handler.add_record("incomes", amount, category, description)

    def add_expense(self):
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the amount.")
        category = input("Enter expense category: ")
        description = input("Enter description: ")
        self.record_handler.add_record("expenses", amount, category, description)

    def set_budget(self):
        category = input("Enter budget category: ")
        while True:
            try:
                limit_amount = float(input("Enter budget limit: "))
                break
            except ValueError:
                print(
                    "Invalid input. Please enter a valid number for the budget limit."
                )
        self.budget_handler.set_budget(category, limit_amount)

    def view_incomes(self):
        self.record_handler.view_records("incomes")

    def view_expenses(self):
        self.record_handler.view_records("expenses")

    def view_budget_progress(self):
        print("Budget progress feature not yet implemented.")

    def clear_all_history(self):
        confirm = input(
            "Are you sure you want to clear all history? This action cannot be undone. (y/n): "
        ).lower()
        if confirm == "y":
            self.record_handler.clear_database()

    def clear_last_entry(self):
        table = input(
            "Which table would you like to clear the last entry from? (incomes/expenses): "
        ).lower()
        if table not in ["incomes", "expenses"]:
            print("Invalid table. Please choose either 'incomes' or 'expenses'.")
        else:
            self.record_handler.clear_last_entry(table)

    def exit_program(self):
        confirm = input("Are you sure you want to exit? (y/n): ").lower()
        if confirm == "y":
            print("Goodbye!")
            exit()
