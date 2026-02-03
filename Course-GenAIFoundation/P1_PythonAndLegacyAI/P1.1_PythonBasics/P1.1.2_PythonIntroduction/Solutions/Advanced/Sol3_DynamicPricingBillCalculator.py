"""
Solution: Advanced Assignment 3 - Dynamic Pricing and Bill Calculator

This solution demonstrates:
- Dictionary lookup for menu items
- Dynamic pricing with multipliers
- Tiered discount logic
- Multi-category tax calculations
- Payment splitting logic
- Complex invoice generation
"""

# Menu and configuration
menu = {
    "Burger": {"base_price": 15.00, "category": "food"},
    "Soda": {"base_price": 3.00, "category": "beverage"},
    "Dessert": {"base_price": 8.00, "category": "food"},
}

time_multipliers = {
    "lunch": 0.9,
    "dinner": 1.1,
    "late_night": 1.3,
}

tax_rates = {
    "food": 0.08,
    "beverage": 0.10,
}

# Input data
order = [
    {"item": "Burger", "quantity": 2},
    {"item": "Soda", "quantity": 2},
    {"item": "Dessert", "quantity": 1},
]

time_period = "dinner"
customer_loyalty_level = 2  # Silver
group_size = 4
payment_method = "card"

# Step 1-3: Calculate itemized costs with dynamic pricing
print("ITEMIZED RECEIPT:")
print("-" * 70)

itemized = []
subtotal = 0

for order_item in order:
    item_name = order_item["item"]
    quantity = order_item["quantity"]
    
    menu_item = menu[item_name]
    base_price = menu_item["base_price"]
    category = menu_item["category"]
    
    # Dynamic pricing
    time_multiplier = time_multipliers[time_period]
    dynamic_price = base_price * time_multiplier
    item_total = dynamic_price * quantity
    
    itemized.append({
        "item": item_name,
        "quantity": quantity,
        "base_price": base_price,
        "dynamic_price": dynamic_price,
        "total": item_total,
        "category": category,
    })
    
    subtotal += item_total
    print("{}x {:12s} @ ${:6.2f} (base ${:6.2f} × {}) = ${:6.2f}".format(quantity, item_name, dynamic_price, base_price, time_multiplier, item_total))

print("-" * 70)
print("Subtotal: ${:.2f}".format(subtotal))

# Step 4-5: Apply discounts
print("\nDISCOUNTS:")
print("-" * 70)

# Tiered discount
if subtotal > 50:
    tiered_discount_pct = 5.0
elif subtotal > 100:
    tiered_discount_pct = 10.0
else:
    tiered_discount_pct = 0

tiered_discount = subtotal * (tiered_discount_pct / 100)

# Loyalty discount (Silver = 2 levels = 5%)
loyalty_discount_pct = customer_loyalty_level * 2.5  # 0->0%, 1->2.5%, 2->5%, 3->7.5%
loyalty_discount = (subtotal - tiered_discount) * (loyalty_discount_pct / 100)

subtotal_after_discount = subtotal - tiered_discount - loyalty_discount

print("Tiered Discount ({:.0f}%): -${:.2f}".format(tiered_discount_pct, tiered_discount))
print("Loyalty Discount ({:.1f}%): -${:.2f}".format(loyalty_discount_pct, loyalty_discount))
print("Subtotal After Discount: ${:.2f}".format(subtotal_after_discount))

# Step 6: Calculate taxes by category
print("\nTAXES:")
print("-" * 70)

tax_by_category = {}
total_tax = 0

for item in itemized:
    category = item["category"]
    if category not in tax_by_category:
        tax_by_category[category] = 0
    
    item_tax = item["total"] * tax_rates.get(category, 0)
    tax_by_category[category] += item_tax
    total_tax += item_tax

for category, tax_amount in tax_by_category.items():
    tax_rate = tax_rates.get(category, 0)
    print("{} Tax ({:.0f}%): ${:.2f}".format(category.capitalize(), tax_rate*100, tax_amount))

# Step 7: Service charge (based on group size)
service_charge_pct = 15 + (group_size - 1) * 1  # Base 15% + 1% per extra person
service_charge = (subtotal_after_discount + total_tax) * (service_charge_pct / 100)

print("Service Charge ({:.0f}% for {} people): ${:.2f}".format(service_charge_pct, group_size, service_charge))

# Step 8: Calculate loyalty points
total_before_service = subtotal_after_discount + total_tax
loyalty_points = int(total_before_service) * (customer_loyalty_level + 1)

# Final total
final_total = total_before_service + service_charge

print("\n" + "=" * 70)
print("TOTAL BILL: ${:.2f}".format(final_total))
print("LOYALTY POINTS EARNED: {} points".format(loyalty_points))
print("=" * 70)

# Step 9: Payment split
print("\nPAYMENT SPLIT ({} people):".format(group_size))
print("-" * 70)

per_person_equal = final_total / group_size
print("Equal split: ${:.2f} each".format(per_person_equal))

# Alternative: proportional to order
print("Alternative (per person): ${:.2f} each".format(final_total / group_size))
print("Total: {} × ${:.2f} = ${:.2f}".format(group_size, per_person_equal, final_total))

# Receipt summary
print("\n" + "=" * 70)
print("PAYMENT METHOD:", payment_method.upper())
print("THANK YOU FOR YOUR VISIT!")
print("=" * 70)
