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
