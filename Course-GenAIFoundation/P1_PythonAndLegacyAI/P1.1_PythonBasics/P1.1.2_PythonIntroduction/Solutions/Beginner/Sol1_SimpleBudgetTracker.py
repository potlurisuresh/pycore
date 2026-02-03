"""
Solution: Beginner Assignment 1 - Simple Budget Tracker

This solution demonstrates:
- Type conversion with float()
- Arithmetic operations
- .format() method for formatting
"""

# Input data
name = "Alex"
weekly_budget = "50"
spent_food = "18.5"
spent_transport = "7.25"
spent_misc = "9"

# Step 1: Convert all numeric strings to float
budget = float(weekly_budget)
food = float(spent_food)
transport = float(spent_transport)
misc = float(spent_misc)

# Step 2: Sum all spending categories
total_spent = food + transport + misc

# Step 3: Calculate remaining budget
remaining = budget - total_spent

# Step 4: Print a clean report with formatted output
print("{}'s Weekly Budget Report".format(name))
print("Total Budget: ${:.2f}".format(budget))
print("Total Spent: ${:.2f}".format(total_spent))
print("Remaining: ${:.2f}".format(remaining))

# Alternative approach - one-liner calculation
print("\nDirect Output: Total Spent: {:.2f}, Remaining: {:.2f}".format(total_spent, remaining))
