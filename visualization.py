import matplotlib.pyplot as plt
import sqlite3


class Visualization:
    def __init__(self, conn):
        self.conn = conn

    def visualize_spending(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT category, SUM(amount) FROM expenses GROUP BY category"
            )
            spending_data = cursor.fetchall()

            if not spending_data:
                print("No spending data available.")
                return

            categories = [row[0] for row in spending_data]
            amounts = [row[1] for row in spending_data]

            print("\nSpending Data:")
            print("Category".ljust(20) + "Amount Spent")
            print("-" * 30)
            for category, amount in zip(categories, amounts):
                print(f"{category:<20} ${amount:.2f}")
            print("-" * 30)

            plt.figure(figsize=(10, 6))
            bars = plt.bar(categories, amounts, color="skyblue", edgecolor="black")

            plt.xlabel("Categories", fontsize=12, fontweight="bold")
            plt.ylabel("Amount Spent ($)", fontsize=12, fontweight="bold")
            plt.title("Spending by Category", fontsize=14, fontweight="bold")

            for bar in bars:
                yval = bar.get_height()
                plt.text(
                    bar.get_x() + bar.get_width() / 2,
                    yval + 5,
                    f"{yval:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=10,
                )

            plt.grid(axis="y", linestyle="--", alpha=0.7)

            plt.xticks(rotation=45, ha="right")

            plt.tight_layout()

            plt.ion()
            plt.show()

            plt.pause(0.001)

            plt.close()

        except sqlite3.Error as e:
            print(f"Error visualizing spending: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
