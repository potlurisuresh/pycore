"""
Mini Project 3: Sales Report Generator
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, numbers, calculations
- P1.1.3: String methods (split, strip), f-strings
- P1.1.4: Dictionaries, lists

Description:
Process sales transactions and calculate totals by salesperson and product.
"""

# Sales data: Date, Salesperson, Product, Quantity, Price
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

# Step 1: Parse transactions into list of dictionaries
transactions = []
for line in sales_data.strip().split('\n'):
    parts = [p.strip() for p in line.split(',')]
    transaction = {
        'date': parts[0],
        'salesperson': parts[1],
        'product': parts[2],
        'quantity': int(parts[3]),
        'price': float(parts[4])
    }
    transaction['total'] = transaction['quantity'] * transaction['price']
    transactions.append(transaction)

print(f"\nTotal Transactions: {len(transactions)}")

# Step 2: Calculate sales by person
sales_by_person = {}
for trans in transactions:
    person = trans['salesperson']
    if person in sales_by_person:
        sales_by_person[person] += trans['total']
    else:
        sales_by_person[person] = trans['total']

print("\nSales by Person:")
for person, total in sales_by_person.items():
    print(f"  {person:10s}: ${total:,.2f}")

# Step 3: Calculate sales by product
sales_by_product = {}
units_by_product = {}
for trans in transactions:
    product = trans['product']
    
    if product in sales_by_product:
        sales_by_product[product] += trans['total']
        units_by_product[product] += trans['quantity']
    else:
        sales_by_product[product] = trans['total']
        units_by_product[product] = trans['quantity']

print("\nSales by Product:")
for product in sales_by_product:
    revenue = sales_by_product[product]
    units = units_by_product[product]
    print(f"  {product:10s}: {units} units, ${revenue:,.2f}")

# Step 4: Find top salesperson
top_person = ""
top_sales = 0
for person, sales in sales_by_person.items():
    if sales > top_sales:
        top_sales = sales
        top_person = person

print(f"\nTop Salesperson: {top_person} (${top_sales:,.2f})")

# Step 5: Calculate total revenue
total_revenue = 0
for trans in transactions:
    total_revenue += trans['total']

print(f"Total Revenue: ${total_revenue:,.2f}")

# Step 6: Calculate average transaction value
avg_transaction = total_revenue / len(transactions)
print(f"Average Transaction: ${avg_transaction:,.2f}")

print("=" * 60)
