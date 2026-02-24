# Week 6 - Exercise 3
# Personal Expense Tracker

expenses = []
category_totals = {}
unique_categories = set()

print("=== Personal Expense Tracker ===")

# Collect 5 expenses
for i in range(1, 6):
    print(f"\nExpense {i}")
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")

    expenses.append((category, amount, date))

    category_totals[category] = category_totals.get(category, 0) + amount
    unique_categories.add(category)


# Calculate statistics
amounts = [expense[1] for expense in expenses]

total_spent = sum(amounts)
average_expense = total_spent / len(amounts)
highest_expense = max(amounts)
lowest_expense = min(amounts)


# Display report
print("\n=== EXPENSE REPORT ===")

print("\nAll Expenses:")
for category, amount, date in expenses:
    print(f"{category} - ${amount:.2f} on {date}")

print("\nSpending by Category:")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")

print("\nUnique Categories:")
print(unique_categories)

print(f"\nTotal Spent: ${total_spent:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Highest Expense: ${highest_expense:.2f}")
print(f"Lowest Expense: ${lowest_expense:.2f}")