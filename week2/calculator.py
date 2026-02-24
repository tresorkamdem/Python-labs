"""
Week 2 - Business Profit Calculator
This script calculates profit and profit margin.
Author: Jean Jacques Kamdem
Course: Python Lab
"""

def calculate_profit(revenue, costs):
    return revenue - costs


def calculate_margin(profit, revenue):
    if revenue == 0:
        return 0
    return (profit / revenue) * 100


def main():
    print("=== Business Profit Calculator ===")

    try:
        revenue = float(input("Enter total revenue: "))
        costs = float(input("Enter total costs: "))

        profit = calculate_profit(revenue, costs)
        margin = calculate_margin(profit, revenue)

        print("\n--- Results ---")
        print(f"Revenue: ${revenue:.2f}")
        print(f"Costs: ${costs:.2f}")
        print(f"Profit: ${profit:.2f}")
        print(f"Profit Margin: {margin:.2f}%")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()