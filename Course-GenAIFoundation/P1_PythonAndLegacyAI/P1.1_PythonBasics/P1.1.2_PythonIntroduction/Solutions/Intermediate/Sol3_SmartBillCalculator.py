"""
Solution: Intermediate Assignment 3 - Smart Bill Calculator

This solution demonstrates:
- Ordered calculation sequence
- Conditional logic for optional charges
- Percentage and arithmetic operations
- Currency formatting
- Division for bill splitting
"""

# Input data
subtotal = 100.00
tax_rate = 0.10  # 10%
service_charge_percent = 15.0  # 15%
tip_percent = 18.0  # 18%
discount_percent = 10.0  # 10%
split_count = 2

# Step 1: Apply discount to subtotal
discount_amount = subtotal * (discount_percent / 100)
subtotal_after_discount = subtotal - discount_amount

print("Subtotal: ${:.2f}".format(subtotal))
print("Discount ({}%): -${:.2f}".format(discount_percent, discount_amount))
print("Subtotal After Discount: ${:.2f}".format(subtotal_after_discount))

# Step 2: Calculate tax on discounted amount
tax_amount = subtotal_after_discount * tax_rate
base_for_service = subtotal_after_discount + tax_amount

print("Tax ({:.0f}%): ${:.2f}".format(tax_rate*100, tax_amount))

# Step 3-4: Calculate service charge on base amount
service_charge = base_for_service * (service_charge_percent / 100)
total_before_tip = base_for_service + service_charge

print("Service Charge ({}%): ${:.2f}".format(service_charge_percent, service_charge))

# Step 5: Calculate tip on total
tip_amount = total_before_tip * (tip_percent / 100)

# Step 6: Calculate final total
final_total = total_before_tip + tip_amount

print("Tip ({}%): ${:.2f}".format(tip_percent, tip_amount))
print("Total: ${:.2f}".format(final_total))

# Step 7: If splitting, divide by split_count
per_person = final_total / split_count

print("\nPer Person (split {}): ${:.2f}".format(split_count, per_person))

# Alternative approach: Breakdown as percentage
print("\n--- Breakdown Summary ---")
print("Original Subtotal: ${:.2f} (100%)".format(subtotal))
print("After Discount: ${:.2f} ({:.1f}%)".format(subtotal_after_discount, (subtotal_after_discount/subtotal)*100))
print("With Tax, Service, Tip: ${:.2f} ({:.1f}%)".format(final_total, (final_total/subtotal)*100))
