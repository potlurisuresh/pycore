"""
Advanced Assignment 3: Dynamic Pricing and Bill Calculator

Scenario:
Compute a group dining bill with time‑based pricing, discounts, taxes, service
charge, and a fair split.

Inputs:
- menu_items (item, base_price, category)
- order (item_name, quantity)
- time_period (lunch/dinner/late_night)
- customer_loyalty_level (0–3)
- group_size, payment_method

Tasks:
1) Apply time multipliers and compute item totals.
2) Apply tiered and loyalty discounts.
3) Compute tax by category + service charge.
4) Produce total, points earned, and per‑person split.

Output:
- Itemized receipt, totals, discounts, taxes, split summary.

Hints:
- Multipliers: {lunch:0.9, dinner:1.1, late_night:1.3}
- Tiered discount based on subtotal.

Rubric:
- Pricing, discounts, tax/service, split, clarity.
"""
