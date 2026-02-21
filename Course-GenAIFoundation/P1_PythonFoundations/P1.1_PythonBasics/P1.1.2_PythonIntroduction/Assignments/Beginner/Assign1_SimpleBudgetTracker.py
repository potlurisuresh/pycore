"""
Beginner Assignment 1: Simple Budget Tracker

Scenario:
You are helping a student track weekly spending and see how much budget remains.

Objective:
Calculate total spent and remaining budget from given inputs.

Inputs:
- name (string)
- weekly_budget (string number)
- spent_food (string number)
- spent_transport (string number)
- spent_misc (string number)

Outputs:
- A short report showing total spent and remaining budget (2 decimals).

Steps / Logic Checklist:
1) Convert all numeric strings to numbers (float).
2) Sum all spending categories.
3) Subtract total spent from weekly budget.
4) Print a clean report using formatted output.

Constraints:
- Assume all numeric inputs are valid numbers.
- Output should be in currency format with two decimals.

Example:
Input: budget="50", food="18.5", transport="7.25", misc="9"
Output: Total Spent: 34.75, Remaining: 15.25

Hints:
- Use float() for conversion.
- Use .format() method or string concatenation for output.

"""
