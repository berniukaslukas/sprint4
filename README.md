# Personal Finance Tracker

A Python application for tracking personal finances, including income, expenses, budget management, and visualizations of spending data. The program allows you to:

- Add income and expenses
- Set and track budget limits
- View income and expense records
- Visualize spending trends by category
- Clear all or last records of income or expenses
- Exit the application safely

## Features

- **Add Income:** Input income amount, category, and description to store income records.
- **Add Expense:** Input expense amount, category, and description to store expense records.
- **Set Budget:** Set budget limits for different categories.
- **View Incomes/Expenses:** View a list of income or expense records.
- **View Budget Progress:** Displays the progress of your budget in different categories (currently not implemented fully).
- **Visualize Spending:** View a graphical representation of your spending by category using a bar chart.
- **Clear History:** Option to clear all records or delete the last entry for incomes or expenses.
- **Exit Program:** Exit the program safely after confirmation.

## Requirements

- Python 3.x
- SQLite3 (for database management)
- `matplotlib` (for visualizations)

You can install the required dependencies using `pip`:

```bash
pip install matplotlib

How to Run
Clone this repository:
bash
Copy code
git clone https://github.com/berniukaslukas/sprint4
cd personal-finance-tracker
Ensure that you have the necessary Python dependencies installed:
bash
Copy code
pip install -r requirements.txt
Run the program:
bash
Copy code
python main.py
The program will display a menu with various options. You can choose an option by entering the corresponding number. The program will continue to show the menu until you select the option to exit.

Usage
Add Income/Expense: Select option 1 to add income or 2 to add an expense. You will be prompted to enter the amount, category, and description.
View Incomes/Expenses: Select option 4 to view your incomes or 5 to view your expenses.
Set Budget: Select option 3 to set budget limits for various categories.
Visualize Spending: Select option 7 to see a bar chart of your spending by category.
Clear History: Option 8 clears all records (be careful!). Option 9 clears the last entry from the selected table (incomes or expenses).
Exit: Option 10 exits the application after confirmation.
Data Storage
The data is stored in an SQLite database. The database will automatically be created when you run the program. The tables used for storing records are:

Incomes: Stores income records with their category and description.
Expenses: Stores expense records with their category and description.
Budgets: Stores budget limits for each category.
