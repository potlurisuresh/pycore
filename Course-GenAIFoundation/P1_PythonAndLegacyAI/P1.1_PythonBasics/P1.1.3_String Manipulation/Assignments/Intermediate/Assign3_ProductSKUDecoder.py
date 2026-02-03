"""
Intermediate Assignment 3: Product SKU Decoder

Scenario:
Process multiple SKUs, validate format, and generate category statistics.

Input:
- sku_batch: "CLOTH-SHIRT42-L|ELECT-PHONE15-M|INVALID|CLOTH-PANT23-XL|FOOD-CHIPS8-S"

Tasks:
1. Split sku_batch by '|' to get individual SKUs
2. Validate each SKU format using regex: r"^[A-Z]+-[A-Z0-9]+-[A-Z]+$"
3. For valid SKUs, extract category, product ID, and size
4. Count products per category
5. Print validation report and category breakdown

Expected Output:
SKU Processing Report
---------------------
Total SKUs: 5
Valid: 4
Invalid: 1

Category Breakdown:
CLOTH: 2 products
ELECT: 1 products
FOOD: 1 products

Valid SKUs:
1. CLOTH-SHIRT42-L (Category: CLOTH, Size: L)
2. ELECT-PHONE15-M (Category: ELECT, Size: M)
3. CLOTH-PANT23-XL (Category: CLOTH, Size: XL)
4. FOOD-CHIPS8-S (Category: FOOD, Size: S)

Hints:
- Use split('|') for SKUs
- Use re.match() with pattern
- Use split('-') on valid SKUs
- Track categories in lists
- Use count() for category totals

Rubric:
- Correct parsing: 20%
- Correct regex validation: 30%
- Correct data extraction: 25%
- Correct category counting: 15%
- Proper output: 10%
"""

# Input data
sku_batch = "CLOTH-SHIRT42-L|ELECT-PHONE15-M|INVALID|CLOTH-PANT23-XL|FOOD-CHIPS8-S"

# Your code here
