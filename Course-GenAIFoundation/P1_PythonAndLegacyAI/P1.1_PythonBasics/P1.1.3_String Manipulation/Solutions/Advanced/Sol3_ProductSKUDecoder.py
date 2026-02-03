"""
Advanced Solution 3: Product SKU Decoder
"""
import re

# Input data
sku_batch = """ELC-2024-M-BLU-001, ELC-2024-L-RED-002, CLO-2023-S-GRN-015
ELC-2024-M-BLU-003, INVALID-SKU, FOO-2025-XL-WHT-099
CLO-2023-M-BLU-020, ELC-2024-M-BLU-005, CLO-2023-L-RED-008"""

# Parse SKUs
all_skus = sku_batch.replace("\n", ", ").split(", ")
all_skus = [s.strip() for s in all_skus if s.strip()]

# Regex for validation
pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{1,2}-[A-Z]{3}-\d{3}$"

# Validate and parse
valid_skus = []
invalid_skus = []
categories = []
years = []
sizes = []
colors = []
ids = []

for sku in all_skus:
    sku_clean = sku.strip()
    if re.match(pattern, sku_clean):
        valid_skus.append(sku_clean)
        parts = sku_clean.split("-")
        categories.append(parts[0])
        years.append(parts[1])
        sizes.append(parts[2])
        colors.append(parts[3])
        ids.append(int(parts[4]))
    else:
        invalid_skus.append(sku)

# Category analysis
unique_categories = []
for cat in categories:
    if cat not in unique_categories:
        unique_categories.append(cat)

category_counts = []
for cat in unique_categories:
    category_counts.append(categories.count(cat))

# Size and color distribution
unique_sizes = []
size_counts = []
for size in sizes:
    if size not in unique_sizes:
        unique_sizes.append(size)
        size_counts.append(sizes.count(size))

unique_colors = []
color_counts = []
for color in colors:
    if color not in unique_colors:
        unique_colors.append(color)
        color_counts.append(colors.count(color))

# Find bestseller
max_color_count = max(color_counts)
bestseller_color = unique_colors[color_counts.index(max_color_count)]

# Detect product series (same category-size-color)
series_detected = []
for i in range(len(valid_skus)):
    for j in range(i + 1, len(valid_skus)):
        if (categories[i] == categories[j] and 
            sizes[i] == sizes[j] and 
            colors[i] == colors[j]):
            combo = f"{categories[i]}-{sizes[i]}-{colors[i]}"
            if combo not in series_detected:
                series_detected.append(combo)

# Detect anomalies
future_dated = []
high_id_alerts = []

for i in range(len(valid_skus)):
    if int(years[i]) > 2024:
        future_dated.append(valid_skus[i])
    if ids[i] > 50:
        high_id_alerts.append(valid_skus[i])

# Print report
print("Inventory Intelligence Report")
print("=" * 50)
print()

print("Validation Summary:")
print(f"Total SKUs: {len(all_skus)}")
print(f"Valid Format: {len(valid_skus)}")
print(f"Invalid Format: {len(invalid_skus)}")
validation_rate = len(valid_skus) * 100.0 / len(all_skus)
print(f"Validation Rate: {validation_rate:.1f}%")
print()

print("Category Breakdown:")
for i in range(len(unique_categories)):
    cat = unique_categories[i]
    count = category_counts[i]
    percentage = count * 100.0 / len(valid_skus)
    
    # Category name
    if cat == "ELC":
        cat_name = "Electronics"
    elif cat == "CLO":
        cat_name = "Clothing"
    elif cat == "FOO":
        cat_name = "Food"
    else:
        cat_name = "Unknown"
    
    print(f"{cat} ({cat_name}): {count} SKUs ({percentage:.1f}%)")
    
    # Find popular combo for this category
    cat_combos = []
    for j in range(len(categories)):
        if categories[j] == cat:
            combo = f"{sizes[j]}-{colors[j]}"
            cat_combos.append(combo)
    
    if len(cat_combos) > 0:
        popular_combo = max(set(cat_combos), key=cat_combos.count)
        print(f"  - Popular: {popular_combo}")
    
    # Special warnings
    if cat == "FOO":
        for year in years:
            if int(year) > 2024:
                print(f"  WARNING: Future Date: {year} detected")
                break
print()

print("Size Distribution:")
for i in range(len(unique_sizes)):
    size = unique_sizes[i]
    count = size_counts[i]
    percentage = count * 100.0 / len(valid_skus)
    print(f"{size}: {count} SKUs ({percentage:.1f}%)")
print()

print("Color Analysis:")
for i in range(len(unique_colors)):
    color = unique_colors[i]
    count = color_counts[i]
    percentage = count * 100.0 / len(valid_skus)
    note = " - BESTSELLER" if color == bestseller_color else ""
    print(f"{color}: {count} SKUs ({percentage:.1f}%{note})")
print()

if len(series_detected) > 0:
    print("Product Series Detected:")
    for series in series_detected:
        print(f"{series} Series (Multiple units in production)")
    print()

print("Anomaly Detection:")
if len(future_dated) > 0:
    for sku in future_dated:
        print(f"WARNING: Future-dated: {sku}")
if len(high_id_alerts) > 0:
    for sku in high_id_alerts:
        id_num = int(sku.split("-")[-1])
        print(f"WARNING: High ID Alert: {sku.split('-')[0]} ID={id_num:03d} (restock needed)")
if len(invalid_skus) > 0:
    for sku in invalid_skus:
        print(f"WARNING: Invalid SKU: {sku}")
print()

print("Inventory Insights:")
# Dominant category
max_cat_count = max(category_counts)
max_cat_index = category_counts.index(max_cat_count)
dominant_cat = unique_categories[max_cat_index]

cat_names = {"ELC": "Electronics", "CLO": "Clothing", "FOO": "Food"}
cat_name = cat_names.get(dominant_cat, dominant_cat)

percentage = max_cat_count * 100.0 / len(valid_skus)
print(f"- {cat_name} ({dominant_cat}) dominates: {percentage:.1f}% of inventory")

max_size = unique_sizes[size_counts.index(max(size_counts))]
print(f"- Size {max_size} most popular across categories")
print(f"- {bestseller_color} color is bestseller")
print()

print("Recommendations:")
if len(future_dated) > 0:
    print("1. Investigate future-dated SKUs")
if len(high_id_alerts) > 0:
    print("2. Review high ID numbers (>50) for restocking")
print(f"3. Focus production on {max_size}-{bestseller_color} combination")
