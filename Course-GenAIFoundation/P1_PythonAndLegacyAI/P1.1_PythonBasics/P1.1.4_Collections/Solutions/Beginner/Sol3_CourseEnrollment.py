"""
Beginner Solution 3: Inventory Stock Manager
"""

# Input data
product_ids = "P001, P002, P001, P003, P002, P004"

# Parse into list
all_products = [p.strip() for p in product_ids.split(',')]

# Use set to find unique items
unique_products = set(all_products)

print(f"All products: {all_products}")
print(f"Unique products: {unique_products}")
print(f"Total scanned: {len(all_products)}")
print(f"Unique items: {len(unique_products)}")
print(f"Duplicates found: {len(all_products) - len(unique_products)}")
