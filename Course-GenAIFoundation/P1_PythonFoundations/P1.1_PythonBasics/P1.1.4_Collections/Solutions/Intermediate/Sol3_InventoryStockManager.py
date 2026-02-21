"""
Intermediate Solution 3: Inventory Stock Manager
"""

# Input data
warehouse_a = "P001, P002, P003, P004, P005"
warehouse_b = "P003, P004, P005, P006, P007"

# Parse into sets
set_a = {p.strip() for p in warehouse_a.split(',')}
set_b = {p.strip() for p in warehouse_b.split(',')}

# Perform set operations
in_both = set_a & set_b  # Intersection
only_in_a = set_a - set_b  # Difference
only_in_b = set_b - set_a  # Difference
all_items = set_a | set_b  # Union

print("Warehouse A:", set_a)
print("Warehouse B:", set_b)
print("\nSet Operations:")
print(f"Items in both warehouses: {in_both}")
print(f"Items only in Warehouse A: {only_in_a}")
print(f"Items only in Warehouse B: {only_in_b}")
print(f"All unique items: {all_items}")
print(f"\nTotal unique items: {len(all_items)}")
