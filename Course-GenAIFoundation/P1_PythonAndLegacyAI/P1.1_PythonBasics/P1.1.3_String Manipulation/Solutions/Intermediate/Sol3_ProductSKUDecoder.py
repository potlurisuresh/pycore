"""
Intermediate Solution 3: Product SKU Decoder
"""
import re

# Input data
sku_batch = "ELC-2024-M-BLU-001, CLO-2023-L-RED-005, INVALID, ELC-2024-S-GRN-003"

# Parse SKUs
skus = sku_batch.split(", ")

# Regex pattern for SKU validation
pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{1,2}-[A-Z]{3}-\d{3}$"

# Initialize lists
valid_skus = []
invalid_skus = []
categories = []
sizes = []

# Validate and parse each SKU
for sku in skus:
    sku_clean = sku.strip()
    if re.match(pattern, sku_clean):
        valid_skus.append(sku_clean)
        parts = sku_clean.split("-")
        categories.append(parts[0])
        sizes.append(parts[2])
    else:
        invalid_skus.append(sku)

# Count category occurrences
category_names = []
category_counts = []
for cat in categories:
    if cat not in category_names:
        category_names.append(cat)
        category_counts.append(categories.count(cat))

# Print formatted output
print("SKU Validation Report")
print("=" * 30)
print(f"Total SKUs: {len(skus)}")
print(f"Valid: {len(valid_skus)}")
print(f"Invalid: {len(invalid_skus)}")
print()
print("Valid SKUs:")
for sku in valid_skus:
    print(f"  - {sku}")
print()
print("Category Statistics:")
for i in range(len(category_names)):
    cat = category_names[i]
    count = category_counts[i]
    if cat == "ELC":
        name = "Electronics"
    elif cat == "CLO":
        name = "Clothing"
    elif cat == "FOO":
        name = "Food"
    else:
        name = "Unknown"
    print(f"  {name} ({cat}): {count} SKU(s)")
