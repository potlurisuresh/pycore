"""
Intermediate Assignment 3: Smart Bill Calculator

Scenario:
A restaurant needs to calculate bills for group dining with multiple payment scenarios:
different tip percentages, service charges, tax calculations, and optional discounts.

Objective:
Calculate final bill amount including tax, service charge, discount, and tip with 
detailed breakdown.

Inputs:
- subtotal (float, base bill amount)
- tax_rate (float, tax percentage like 0.10 for 10%)
- service_charge_percent (float, optional service charge as percentage)
- tip_percent (float, tip percentage)
- discount_percent (float, optional discount percentage)
- split_count (integer, number of people splitting)

Outputs:
- Breakdown: subtotal, tax, service charge, discount, tip
- Total amount due
- Per-person amount (if splitting)

Steps / Logic Checklist:
1) Apply discount to subtotal (if any).
2) Calculate tax on the discounted amount.
3) Calculate subtotal + tax = base for service charge.
4) Calculate service charge on base amount.
5) Calculate tip on total (subtotal + tax + service) or specify tip base.
6) Calculate final total = subtotal - discount + tax + service + tip.
7) If splitting, divide by split_count.
8) Print detailed breakdown.

Constraints:
- All numeric inputs are valid positive numbers.
- Discount and tip rates can be 0.
- split_count is at least 1.
- Tax is applied only to discounted subtotal.

Example:
Input: subtotal=100, tax_rate=0.10, service_percent=15, tip_percent=18, 
       discount_percent=10, split_count=2
Output:
Subtotal: 100.00, Discount: -10.00
Subtotal After Discount: 90.00
Tax (10%): 9.00
Service Charge (15%): 13.50
Tip (18%): 21.69
Total: 134.19
Per Person (split 2): 67.10

Hints:
- Calculate in the correct order: discount → tax → service → tip.
- Use round() for currency precision.
- Use if statements for optional charges.
- Test with different scenarios.

Rubric:
- Discount calculation: 15%
- Tax calculation on correct base: 15%
- Service charge calculation: 15%
- Tip calculation: 15%
- Final total calculation: 15%
- Per-person split calculation: 15%
- Formatted breakdown output: 10%

"""
