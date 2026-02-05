"""
Solution: Advanced Assignment 3 - Dynamic Pricing and Bill Calculator (Concise)
"""

menu_items = {
    "Burger": {"base_price": 15.00, "category": "food"},
    "Soda": {"base_price": 3.00, "category": "beverage"},
    "Dessert": {"base_price": 8.00, "category": "food"},
}

time_multipliers = {"lunch": 0.9, "dinner": 1.1, "late_night": 1.3}
tax_rates = {"food": 0.08, "beverage": 0.10}

order = [
    {"item": "Burger", "quantity": 2},
    {"item": "Soda", "quantity": 2},
    {"item": "Dessert", "quantity": 1},
]

time_period = "dinner"
customer_loyalty_level = 2  # 0-3
group_size = 4
payment_method = "card"

def tiered_discount(subtotal):
    if subtotal > 100:
        return 0.10
    if subtotal > 50:
        return 0.05
    return 0.0

# Itemized costs
itemized = []
subtotal = 0
for item in order:
    name = item["item"]
    qty = item["quantity"]
    base = menu_items[name]["base_price"]
    category = menu_items[name]["category"]
    price = base * time_multipliers[time_period]
    total = price * qty
    subtotal += total
    itemized.append((name, qty, price, total, category))

discount = subtotal * tiered_discount(subtotal)
loyalty_discount = (subtotal - discount) * (customer_loyalty_level * 0.025)
after_discount = subtotal - discount - loyalty_discount

# Taxes by category
tax_total = 0
for _, _, _, total, category in itemized:
    tax_total += total * tax_rates.get(category, 0)

service_charge_pct = min(25, 15 + max(0, group_size - 1))
service_charge = (after_discount + tax_total) * (service_charge_pct / 100)

total = after_discount + tax_total + service_charge
per_person = total / group_size
loyalty_points = int(total) * (customer_loyalty_level + 1)

print("Itemized Receipt")
print("=" * 48)
for name, qty, price, total_item, _ in itemized:
    print(f"{qty}x {name:10s} @ ${price:.2f} = ${total_item:.2f}")

print("\nSubtotal: ${:.2f}".format(subtotal))
print("Discount: -${:.2f}".format(discount))
print("Loyalty: -${:.2f}".format(loyalty_discount))
print("Tax: ${:.2f}".format(tax_total))
print("Service Charge ({}%): ${:.2f}".format(service_charge_pct, service_charge))
print("Total: ${:.2f}".format(total))
print("Per Person ({}): ${:.2f}".format(group_size, per_person))
print("Loyalty Points: {}".format(loyalty_points))
print("Payment Method:", payment_method.upper())