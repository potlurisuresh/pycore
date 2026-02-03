"""
Intermediate Assignment 1: Budget Tracker with Statistics

Scenario:
A financial app tracks spending across multiple months and categories, helping users understand 
spending patterns and compare monthly budgets.

Objective:
Analyze spending data across multiple months, calculate monthly totals, averages, and identify 
the highest spending month.

Inputs:
- monthly_data (dictionary with month names as keys and spending dictionaries as values)
  Example: {"January": {"food": 150, "transport": 80, "misc": 50}, "February": {...}}

Outputs:
- Total spent per month
- Average spending per month
- Month with highest spending
- Category breakdown for highest spending month

Steps / Logic Checklist:
1) Parse the dictionary to extract monthly data.
2) Calculate total spending for each month (sum all categories).
3) Calculate the average spending across all months.
4) Find the month with maximum total spending.
5) Extract and display category breakdown for highest spending month.
6) Print formatted report with all statistics.

Constraints:
- At least 2 months of data.
- Each month has at least 2 spending categories.
- All values are positive numbers.

Example:
Input: {"January": {"food": 150, "transport": 80, "misc": 50}, 
        "February": {"food": 160, "transport": 90, "misc": 40}}
Output: 
January Total: 280, February Total: 290
Average: 285
Highest Month: February (290)
Categories: food=160, transport=90, misc=40

Hints:
- Use dictionary iteration (keys(), values(), items()).
- Use max() or comparison logic to find highest spending.
- Use sum() for calculating totals.
- Use .format() method or string concatenation for formatting.

Rubric:
- Dictionary parsing and month iteration: 20%
- Total and average calculations: 20%
- Finding highest spending month: 20%
- Category breakdown extraction: 20%
- Formatted output: 20%

"""
