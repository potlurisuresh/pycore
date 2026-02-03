"""
Beginner Assignment 4: Customer Feedback Cleaner

Scenario:
Customer feedback contains common abbreviations that need to be standardized.

Input:
- feedback: "prod is gr8! but svc was avg"

Tasks:
1. Replace "prod" with "product" using replace()
2. Replace "gr8" with "great" using replace()
3. Replace "svc" with "service" using replace()
4. Replace "avg" with "average" using replace()
5. Print the cleaned feedback

Expected Output:
product is great! but service was average

Hints:
- Use replace() method multiple times
- Can chain: text.replace().replace()
- Order doesn't matter for non-overlapping replacements

Rubric:
- Correct replacement of all 4 terms: 80%
- Proper output: 20%
"""

# Input data
feedback = "prod is gr8! but svc was avg"

# Your code here
