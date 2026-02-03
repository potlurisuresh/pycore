"""
Advanced Assignment 3: Dynamic Pricing and Bill Calculator

Scenario:
A restaurant uses dynamic pricing where prices vary by time period (peak/off-peak),
offers tiered discounts based on total bill, applies loyalty rewards, and calculates
complex taxes. The system must handle group bills with payment splits and provide
detailed audit trails.

Objective:
Calculate bills for group dining with dynamic pricing, loyalty discounts, tiered
discounts, complex tax scenarios, payment splitting with fair calculation, and
generate detailed invoice.

Inputs:
- menu_items (list of dicts: {item, base_price, category, time_period})
- order (list of dicts: {item_name, quantity, order_time})
- time_period (string: 'lunch', 'dinner', 'late_night')
- customer_loyalty_level (int: 0-3, where 3 is VIP)
- group_size (integer, number of people splitting)
- payment_method (string: 'cash', 'card', 'digital')
- special_requests (list of strings: discounts, promos)

Outputs:
- Itemized breakdown with dynamic pricing
- Subtotal with pricing details
- Tiered discount amount
- Loyalty reward amount
- Tax breakdown (multiple tax rates by item category)
- Service charge (varies by group size)
- Total bill amount
- Per-person cost (with and without rounding variations)
- Payment split details (who pays what)
- Loyalty points earned
- Receipt summary

Steps / Logic Checklist:
1) Parse menu items and lookup prices.
2) Calculate item costs with dynamic pricing (base × time multiplier).
3) Apply quantity to each item.
4) Calculate subtotal.
5) Determine tiered discount based on subtotal amount.
6) Apply loyalty discount based on customer level.
7) Apply special promo codes (if any).
8) Calculate tax per category (different rates for food/beverage/service).
9) Calculate service charge based on group size and subtotal.
10) Calculate loyalty points earned.
11) Calculate final total.
12) Generate split calculations (equal split, proportional split).
13) Format detailed invoice.

Constraints:
- Group size minimum 1, maximum 20.
- Loyalty levels 0-3 (0=none, 1=bronze, 2=silver, 3=gold).
- All prices are positive floats.
- Tax rates vary by category (0-20%).
- Service charge 0-25% based on group size.

Example:
Input: Orders: [("Burger", 2, "dinner"), ("Soda", 2, "dinner"), ("Dessert", 1, "dinner")]
Menu: Base Burger $15, Soda $3, Dessert $8 (Dinner multiplier: 1.1x)
Customer: Loyalty level 2 (Silver), Group size 4, Card payment
Time: Dinner (peak hours)

Output:
ITEMIZED RECEIPT:
2x Burger @ $16.50 (base $15 × 1.1) = $33.00
2x Soda @ $3.30 (base $3 × 1.1) = $6.60
1x Dessert @ $8.80 (base $8 × 1.1) = $8.80
Subtotal: $48.40

DISCOUNTS:
Tiered Discount (40-50 range): -$2.42
Loyalty Discount (Silver 5%): -$2.30
Subtotal After Discount: $43.68

TAXES:
Food Tax (8%): $3.49
Beverage Tax (10%): $0.66
Service Charge (18% for 4 people): $7.86
Total Tax/Charges: $11.51

TOTAL BILL: $55.19
LOYALTY POINTS EARNED: 55 points

PAYMENT SPLIT (4 people):
Equal split: $13.80 each
Alternative (proportional to orders): [User 1: $13.80, User 2: $13.80, ...]

Hints:
- Use dictionary lookup for menu items.
- Create time multiplier map: {"lunch": 0.9, "dinner": 1.1, "late_night": 1.3}
- Tiered discounts: if subtotal > 50: discount = 5%, elif > 100: discount = 10%
- Tax per category requires categorizing each item.
- Loyalty points: floor(total) × multiplier (1x/2x/3x by level)
- Use round() for currency precision.

Rubric:
- Menu item lookup and quantity processing: 10%
- Dynamic pricing calculation: 12%
- Tiered discount logic: 10%
- Loyalty discount and points: 10%
- Multi-category tax calculation: 12%
- Service charge by group size: 10%
- Payment split calculations: 12%
- Invoice formatting and clarity: 12%
- Handling edge cases and constraints: 2%

"""
