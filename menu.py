class Menu:
    def __init__(self, handlers):
        self.handlers = handlers

    def display(self):
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Incomes")
        print("5. View Expenses")
        print("6. View Budget Progress")
        print("7. Visualize Spending")
        print("8. Clear All History")
        print("9. Clear Last Entry")
        print("10. Exit")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 10:
                    return choice
                else:
                    print("Invalid choice. Please select a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def run(self):
        while True:
            self.display()
            choice = self.get_choice()

            if choice == 1:
                self.handlers.add_income()
            elif choice == 2:
                self.handlers.add_expense()
            elif choice == 3:
                self.handlers.set_budget()
            elif choice == 4:
                self.handlers.view_incomes()
            elif choice == 5:
                self.handlers.view_expenses()
            elif choice == 6:
                self.handlers.view_budget_progress()
            elif choice == 7:
                self.handlers.visualize_spending()
            elif choice == 8:
                self.handlers.clear_all_history()
            elif choice == 9:
                self.handlers.clear_last_entry()
            elif choice == 10:
                self.handlers.exit_program()
                break
