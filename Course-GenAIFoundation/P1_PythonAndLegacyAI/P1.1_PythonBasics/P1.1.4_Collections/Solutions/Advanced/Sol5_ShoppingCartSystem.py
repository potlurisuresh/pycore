"""
Advanced Solution 5: Shopping Cart System
"""

# Input data
orders_data = """C001,Order1:Apple:1.50:10,Banana:0.75:5
C001,Order2:Orange:1.20:8,Apple:1.50:3
C002,Order1:Banana:0.75:20,Orange:1.20:15
C003,Order1:Apple:1.50:5
C002,Order2:Apple:1.50:12,Banana:0.75:8"""

# Build customer structure
customers = {}
item_popularity = {}

for line in orders_data.split('\n'):
    customer_id, order_data = line.split(',', 1)
    
    if customer_id not in customers:
        customers[customer_id] = {'orders': [], 'lifetime_value': 0}
    
    order_items = []
    order_total = 0
    
    # Split order data: first part is OrderX:Item:Price:Qty, rest are Item:Price:Qty
    items = order_data.split(',')
    for i, item in enumerate(items):
        parts = item.split(':')
        if i == 0:
            # First item has order_id: Order1:Apple:1.50:10
            order_id, name, price, qty = parts[0], parts[1], parts[2], parts[3]
        else:
            # Subsequent items: Banana:0.75:5
            name, price, qty = parts[0], parts[1], parts[2]
        
        price = float(price)
        qty = int(qty)
        subtotal = price * qty
        
        order_items.append({'name': name, 'price': price, 'qty': qty, 'subtotal': subtotal})
        order_total += subtotal
        
        # Track popularity
        item_popularity[name] = item_popularity.get(name, 0) + qty
    
    # Apply discount tiers
    discount = 0
    if order_total > 200:
        discount = 0.20
    elif order_total > 100:
        discount = 0.10
    
    final_total = order_total * (1 - discount)
    
    customers[customer_id]['orders'].append({
        'items': order_items,
        'subtotal': order_total,
        'discount': discount * 100,
        'final_total': final_total
    })
    customers[customer_id]['lifetime_value'] += final_total

# Find best customer
best_customer = max(customers.items(), key=lambda x: x[1]['lifetime_value'])

# Find most popular item
most_popular = max(item_popularity.items(), key=lambda x: x[1])

print("Customer Orders:")
for cust_id, data in customers.items():
    print(f"\n{cust_id} (Lifetime Value: ${data['lifetime_value']:.2f}):")
    for i, order in enumerate(data['orders'], 1):
        print(f"  Order {i}: ${order['subtotal']:.2f} - {order['discount']:.0f}% discount = ${order['final_total']:.2f}")

print(f"\nBest Customer: {best_customer[0]} (${best_customer[1]['lifetime_value']:.2f})")
print(f"Most Popular Item: {most_popular[0]} ({most_popular[1]} units sold)")
