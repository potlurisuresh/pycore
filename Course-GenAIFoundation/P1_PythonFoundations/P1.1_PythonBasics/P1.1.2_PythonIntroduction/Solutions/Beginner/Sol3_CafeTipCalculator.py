"""
Solution: Beginner Assignment 3 - Cafe Tip Calculator

This solution demonstrates:
- Type conversion with float()
- Percentage calculation
- Currency formatting with .format() method
"""

# Input data
bill_amount = "24.75"
tip_percent = 10

# Step 1: Convert bill_amount to float
bill = float(bill_amount)

# Step 2: Calculate tip as a percentage
tip_amount = bill * (tip_percent / 100)

# Step 3: Calculate total
total = bill + tip_amount

# Step 4: Print results with two decimal places
print("Bill Amount: ${:.2f}".format(bill))
print("Tip Percent: {}%".format(tip_percent))
print("Tip: ${:.2f}".format(tip_amount))
print("Total: ${:.2f}".format(total))

# Alternative approach - with different inputs
print("\n--- Another Example ---")
bill_2 = float("50.00")
tip_percent_2 = 15
tip_2 = bill_2 * (tip_percent_2 / 100)
total_2 = bill_2 + tip_2
print("Tip: {:.2f}, Total: {:.2f}".format(tip_2, total_2))
