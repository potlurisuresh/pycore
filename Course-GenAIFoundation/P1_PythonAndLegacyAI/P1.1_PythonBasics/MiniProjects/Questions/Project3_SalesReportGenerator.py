"""
Mini Project 3: Sales Report Generator
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, numbers, calculations
- P1.1.3: String methods (split, strip), f-strings
- P1.1.4: Dictionaries, lists

Description:
Process sales transaction data to generate a sales report.
The program should:
1. Parse sales data into list of dictionaries
2. Calculate total sales by each salesperson
3. Calculate total sales by each product
4. Find the top salesperson
5. Calculate total revenue and average transaction value

Expected Output:
============================================================
SALES REPORT GENERATOR
============================================================

Total Transactions: 8

Sales by Person:
  Alice     : $2,900.00
  Bob       : $2,025.00
  Carol     : $475.00

Sales by Product:
  Laptop    : 3 units, $3,600.00
  Mouse     : 15 units, $375.00
  Keyboard  : 5 units, $375.00
  Monitor   : 3 units, $1,050.00

Top Salesperson: Alice ($2,900.00)
Total Revenue: $5,400.00
Average Transaction: $675.00
============================================================
"""

# Sales data - DO NOT MODIFY
# Format: Date, Salesperson, Product, Quantity, Price
sales_data = """2026-02-01, Alice, Laptop, 2, 1200.00
2026-02-01, Bob, Mouse, 5, 25.00
2026-02-01, Carol, Keyboard, 3, 75.00
2026-02-02, Alice, Monitor, 1, 350.00
2026-02-02, Bob, Laptop, 1, 1200.00
2026-02-02, Carol, Mouse, 10, 25.00
2026-02-03, Alice, Keyboard, 2, 75.00
2026-02-03, Bob, Monitor, 2, 350.00"""

print("=" * 60)
print("SALES REPORT GENERATOR")
print("=" * 60)

# TODO: Step 1 - Parse transactions into list of dictionaries
# Create an empty list called 'transactions'
# Split sales_data by newline to get each line
# For each line:
#   - Split by comma and strip whitespace
#   - Create a dictionary with keys: date, salesperson, product, quantity, price
#   - Calculate total = quantity * price
#   - Add dictionary to transactions list

transactions = []
# YOUR CODE HERE


print(f"\nTotal Transactions: {len(transactions)}")

# TODO: Step 2 - Calculate sales by person
# Create an empty dictionary 'sales_by_person'
# Loop through transactions
# For each transaction, add the total to the salesperson's count
# If salesperson not in dictionary, initialize to 0 first

sales_by_person = {}
# YOUR CODE HERE


print("\nSales by Person:")
for person, total in sales_by_person.items():
    print(f"  {person:10s}: ${total:,.2f}")

# TODO: Step 3 - Calculate sales by product
# Create two dictionaries: 'sales_by_product' and 'units_by_product'
# Loop through transactions
# For each product, track total revenue and units sold

sales_by_product = {}
units_by_product = {}
# YOUR CODE HERE


print("\nSales by Product:")
for product in sales_by_product:
    revenue = sales_by_product[product]
    units = units_by_product[product]
    print(f"  {product:10s}: {units} units, ${revenue:,.2f}")

# TODO: Step 4 - Find top salesperson
# Loop through sales_by_person
# Find the person with highest sales
# Store in 'top_person' and 'top_sales'

top_person = ""
top_sales = 0
# YOUR CODE HERE


print(f"\nTop Salesperson: {top_person} (${top_sales:,.2f})")

# TODO: Step 5 - Calculate total revenue
# Loop through all transactions and sum up the totals

total_revenue = 0
# YOUR CODE HERE


print(f"Total Revenue: ${total_revenue:,.2f}")

# TODO: Step 6 - Calculate average transaction value
# Divide total_revenue by number of transactions

avg_transaction = 0
# YOUR CODE HERE


print(f"Average Transaction: ${avg_transaction:,.2f}")

print("=" * 60)
