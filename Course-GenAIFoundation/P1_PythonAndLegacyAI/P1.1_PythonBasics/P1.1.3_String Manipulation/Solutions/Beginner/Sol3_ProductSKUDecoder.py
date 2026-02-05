"""
Beginner Solution 3: Product SKU Decoder
"""

# Input data
sku = "ELC-2024-M-BLU-001"

# Parse SKU by splitting on dashes
parts = sku.split("-")

# Extract components
category = parts[0]
year = parts[1]
size = parts[2]
color = parts[3]
product_id = parts[4]

# Decode category
if category == "ELC":
    category_name = "Electronics"
elif category == "CLO":
    category_name = "Clothing"
elif category == "FOO":
    category_name = "Food"
else:
    category_name = "Unknown"

# Decode color
if color == "BLU":
    color_name = "Blue"
elif color == "RED":
    color_name = "Red"
elif color == "GRN":
    color_name = "Green"
elif color == "WHT":
    color_name = "White"
else:
    color_name = "Unknown"

# Print formatted output
print("Product SKU Decoder")
print("=" * 20)
print(f"SKU: {sku}")
print(f"Category: {category_name} ({category})")
print(f"Year: {year}")
print(f"Size: {size}")
print(f"Color: {color_name} ({color})")
print(f"Product ID: {product_id}")
