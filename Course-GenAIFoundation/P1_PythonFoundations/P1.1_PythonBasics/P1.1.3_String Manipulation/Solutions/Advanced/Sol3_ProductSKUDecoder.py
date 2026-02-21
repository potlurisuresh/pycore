"""
Advanced Solution 3: Product SKU Decoder (Concise)
"""
import re

# Input data
sku_batch = """ELC-2024-M-BLU-001, ELC-2024-L-RED-002, CLO-2023-S-GRN-015
ELC-2024-M-BLU-003, INVALID-SKU, FOO-2025-XL-WHT-099
CLO-2023-M-BLU-020, ELC-2024-M-BLU-005, CLO-2023-L-RED-008"""

all_skus = [s.strip() for s in sku_batch.replace("\n", ", ").split(", ") if s.strip()]
pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{1,2}-[A-Z]{3}-\d{3}$"

CATEGORY = {"ELC": "Electronics", "CLO": "Clothing", "FOO": "Food"}
SIZE = {"S": "Small", "M": "Medium", "L": "Large", "XL": "Extra Large"}
COLOR = {"BLU": "Blue", "RED": "Red", "GRN": "Green", "WHT": "White"}
YEAR = "4-digit year"

valid = []
invalid = []
parts_list = []
for sku in all_skus:
    if re.match(pattern, sku):
        parts = sku.split("-")
        parts_list.append(parts)
        valid.append(sku)
    else:
        invalid.append(sku)

categories = [p[0] for p in parts_list]
years = [int(p[1]) for p in parts_list]
sizes = [p[2] for p in parts_list]
colors = [p[3] for p in parts_list]
ids = [int(p[4]) for p in parts_list]

def count_map(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

cat_counts = count_map(categories)
size_counts = count_map(sizes)
color_counts = count_map(colors)

series = set()
for p in parts_list:
    series.add(f"{p[0]}-{p[2]}-{p[3]}")

future_dated = [valid[i] for i, y in enumerate(years) if y > 2024]
high_id = [valid[i] for i, num in enumerate(ids) if num > 50]

print("Inventory Intelligence Report")
print("=" * 48)
print(f"Total: {len(all_skus)} | Valid: {len(valid)} | Invalid: {len(invalid)}")

print("\nCategory Breakdown:")
for cat, cnt in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0])):
    name = CATEGORY.get(cat, "Unknown")
    print(f"- {cat} ({name}): {cnt}")

print("\nSize Distribution:")
for size, cnt in sorted(size_counts.items(), key=lambda x: (-x[1], x[0])):
    print(f"- {size}: {cnt}")

print("\nColor Distribution:")
for color, cnt in sorted(color_counts.items(), key=lambda x: (-x[1], x[0])):
    print(f"- {color}: {cnt}")

print("\nSeries (Category-Size-Color):")
for combo in sorted(series):
    print(f"- {combo}")

print("\nAnomalies:")
for sku in future_dated:
    print(f"- Future-dated: {sku}")
for sku in high_id:
    print(f"- High ID: {sku}")
for sku in invalid:
    print(f"- Invalid: {sku}")

if valid:
    top_cat = max(cat_counts, key=cat_counts.get)
    top_size = max(size_counts, key=size_counts.get)
    top_color = max(color_counts, key=color_counts.get)
    print("\nRecommendations:")
    print(f"- Focus on {top_cat} / {top_size} / {top_color} combinations")
    if future_dated:
        print("- Review future-dated SKUs")
    if high_id:
        print("- Investigate high ID ranges for restocking")
