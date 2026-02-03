"""
Beginner Solution 5: Shopping Cart System
"""

# Input data
cart_items = "Apple:1.50, Banana:0.75, Orange:1.20"

# Parse into dictionary
cart = {}
for item in cart_items.split(','):
    name, price = item.strip().split(':')
    cart[name] = float(price)

# Calculate total
total = sum(cart.values())

print("Shopping Cart:")
for item, price in cart.items():
    print(f"{item}: ${price:.2f}")
print(f"\nTotal: ${total:.2f}")
print(f"Items in cart: {len(cart)}")
