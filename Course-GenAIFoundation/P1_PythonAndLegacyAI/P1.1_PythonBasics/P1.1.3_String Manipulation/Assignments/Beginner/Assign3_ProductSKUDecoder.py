"""
Beginner Assignment 3: Product SKU Decoder

Scenario:
Your warehouse uses SKU codes in the format "CATEGORY-PRODUCTID-SIZE".
Parse a SKU to extract its components.

Input:
- sku: "CLOTH-SHIRT42-L"

Tasks:
1. Split the SKU by '-' to get parts
2. Extract category (first part)
3. Extract product ID (second part)
4. Extract size (third part)
5. Print each component

Expected Output:
Category: CLOTH
Product ID: SHIRT42
Size: L

Hints:
- Use split('-') to break the SKU
- Use list indexing [0], [1], [2]
- Use f-strings for output

Rubric:
- Correct splitting: 40%
- Correct extraction of all parts: 40%
- Proper formatted output: 20%
"""

# Input data
sku = "CLOTH-SHIRT42-L"

# Your code here
