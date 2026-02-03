"""
Solution: Intermediate Assignment 1 - Budget Tracker with Statistics

This solution demonstrates:
- Dictionary parsing and iteration
- Nested data structure handling
- Sum and average calculations
- Finding maximum values
- Dictionary comprehensions
"""

# Input data: Multi-month spending data
spending_data = {
    "January": {"food": 150, "transport": 80, "misc": 50},
    "February": {"food": 160, "transport": 90, "misc": 40},
    "March": {"food": 155, "transport": 85, "misc": 60},
}

# Step 1-2: Parse dictionary and calculate monthly totals
monthly_totals = {}

for month, categories in spending_data.items():
    total = sum(categories.values())
    monthly_totals[month] = total
    print("{}: Total = ${}".format(month, total))

# Step 3: Calculate average spending across all months
total_spent = sum(monthly_totals.values())
avg_spending = total_spent / len(monthly_totals)
print("\nAverage Monthly Spending: ${:.2f}".format(avg_spending))

# Step 4: Find month with maximum spending
highest_month = max(monthly_totals, key=monthly_totals.get)
highest_amount = monthly_totals[highest_month]
print("Highest Spending Month: {} (${})".format(highest_month, highest_amount))

# Step 5: Extract and display category breakdown for highest spending month
print("\nCategory Breakdown for {}:".format(highest_month))
for category, amount in spending_data[highest_month].items():
    print("  {}: ${}".format(category, amount))

# Alternative approach using dict comprehension
print("\n--- Alternative Approach ---")
monthly_totals_alt = {month: sum(cats.values()) for month, cats in spending_data.items()}
print("All months: {}".format(monthly_totals_alt))
