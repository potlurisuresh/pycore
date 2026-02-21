"""
Advanced Assignment 3: Product SKU Decoder

Scenario:
Build an inventory intelligence system that decodes SKUs, validates formats,
detects anomalies, generates category insights, and identifies restocking needs.

Input:
- sku_batch: Multi-line SKU codes
  "ELC-2024-M-BLU-001, ELC-2024-L-RED-002, CLO-2023-S-GRN-015
   ELC-2024-M-BLU-003, INVALID-SKU, FOO-2025-XL-WHT-099
   CLO-2023-M-BLU-020, ELC-2024-M-BLU-005, CLO-2023-L-RED-008"

SKU Format: CATEGORY-YEAR-SIZE-COLOR-ID
- CATEGORY: 3 uppercase letters (ELC=Electronics, CLO=Clothing, FOO=Food)
- YEAR: 4 digits
- SIZE: S, M, L, XL
- COLOR: 3 uppercase letters (BLU, RED, GRN, WHT)
- ID: 3 digits (001-999)

Tasks:
1. Parse and validate all SKUs using regex: r"^[A-Z]{3}-\d{4}-[A-Z]{1,2}-[A-Z]{3}-\d{3}$"
2. Decode each component (category, year, size, color, ID)
3. Detect product patterns:
   - Most common category
   - Size distribution
   - Color popularity
   - Year trends
4. Find duplicate tracking:
   - Same product (category-size-color) with multiple IDs
   - Inventory series (sequential IDs)
5. Identify anomalies:
   - Future-dated products (YEAR > 2024)
   - Unusual ID ranges (ID > 050 may need restocking)
   - Format violations
6. Generate inventory intelligence report with actionable insights

Expected Output:
Inventory Intelligence Report
==============================

Validation Summary:
Total SKUs: 9
Valid Format: 8
Invalid Format: 1
Validation Rate: 88.9%

Category Breakdown:
ELC (Electronics): 5 SKUs (62.5%)
  - 2024 Models: 5 units
  - Popular: M-BLU (3 units)
  - ID Range: 001-005 (ACTIVE SERIES)

CLO (Clothing): 3 SKUs (37.5%)
  - 2023 Models: 3 units
  - Popular: M-BLU (1 units)
  - ID Range: 008-020 (SCATTERED)

FOO (Food): 1 SKUs (12.5%)
  WARNING: Future Date: 2025 detected
  - ID: 099 (HIGH - RESTOCK ALERT)

Size Distribution:
M: 4 SKUs (50.0%)
L: 2 SKUs (25.0%)
S: 1 SKUs (12.5%)
XL: 1 SKUs (12.5%)

Color Analysis:
BLU: 5 SKUs (62.5% - BESTSELLER)
RED: 2 SKUs (25.0%)
GRN: 1 SKUs (12.5%)
WHT: 1 SKUs (12.5%)

Product Series Detected:
ELC-M-BLU Series: 001, 003, 005 (Sequential - Active Production)

Anomaly Detection:
WARNING: Future-dated: FOO-2025-XL-WHT-099
WARNING: High ID Alert: FOO ID=099 (likely needs restocking)
WARNING: Invalid SKU: INVALID-SKU

Inventory Insights:
- Electronics (ELC) dominates: 62.5% of valid inventory
- Size M most popular across categories
- BLU color is bestseller (62.5%)
- ELC-M-BLU shows sequential production (healthy)
- CLO items scattered (IDs: 8, 15, 20) - possible overstock

Recommendations:
1. Investigate future-dated SKU: FOO-2025
2. Review high ID numbers (>50) for restocking
3. Focus production on M-BLU combination
4. Audit CLO inventory for overstock

Hints:
- Use comprehensive regex validation
- Parse components with split()
- Track patterns using parallel lists
- Detect sequential IDs (differences)
- Categorize insights clearly

Rubric:
- Validation accuracy: 15%
- Component parsing: 15%
- Pattern detection: 20%
- Anomaly identification: 25%
- Actionable insights: 25%
"""

# Input data
sku_batch = """ELC-2024-M-BLU-001, ELC-2024-L-RED-002, CLO-2023-S-GRN-015
ELC-2024-M-BLU-003, INVALID-SKU, FOO-2025-XL-WHT-099
CLO-2023-M-BLU-020, ELC-2024-M-BLU-005, CLO-2023-L-RED-008"""

# Your code here
