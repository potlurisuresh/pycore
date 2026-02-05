"""
Intermediate Solution 5: Shopping Cart System
"""

# Input data
carts_data = """Cart1:Apple:1.50:3,Banana:0.75:5
Cart2:Orange:1.20:2,Apple:1.50:1
Cart3:Banana:0.75:4,Orange:1.20:3"""

# Process carts
carts = []
grand_total = 0

for line in carts_data.split('\n'):
    cart_id, items_str = line.split(':', 1)
    items = []
    cart_total = 0
    
    for item in items_str.split(','):
        name, price, qty = item.split(':')
        price = float(price)
        qty = int(qty)
        subtotal = price * qty
        
        items.append({
            'name': name,
            'price': price,
            'quantity': qty,
            'subtotal': subtotal
        })
        cart_total += subtotal
    
    carts.append({
        'id': cart_id,
        'items': items,
        'total': cart_total
    })
    grand_total += cart_total

# Find most expensive cart
most_expensive = max(carts, key=lambda x: x['total'])

print("Shopping Carts:")
for cart in carts:
    print(f"\n{cart['id']} - Total: ${cart['total']:.2f}")
    for item in cart['items']:
        print(f"  {item['name']}: {item['quantity']} x ${item['price']:.2f} = ${item['subtotal']:.2f}")

print(f"\nGrand Total: ${grand_total:.2f}")
print(f"Most expensive cart: {most_expensive['id']} (${most_expensive['total']:.2f})")
