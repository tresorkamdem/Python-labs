"""
Week 3 - Control Flow
Understanding conditions and loops in Python
"""

# Example 1: Simple condition

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Example 2: Profit check

revenue = 5000
costs = 3000
profit = revenue - costs

if profit > 0:
    print("Business is profitable.")
elif profit == 0:
    print("Break-even.")
else:
    print("Business is making a loss.")