"""
Beginner Assignment 2: Email Validator

Scenario:
Clean and validate a user-submitted email address for your signup form.

Input:
- email: "  User.Name@Example.COM  "

Tasks:
1. Remove leading and trailing whitespace using strip()
2. Convert to lowercase using lower()
3. Check if '@' symbol exists using 'in' operator
4. Check if '.' exists after '@' 
5. Print "Valid" if both conditions are met, otherwise "Invalid"

Expected Output:
Cleaned: user.name@example.com
Status: Valid

Hints:
- Use strip() and lower() for cleaning
- Use 'in' to check for characters
- Use split('@') to check for '.' after @
- Use if-else for validation

Rubric:
- Correct cleaning: 30%
- Correct @ check: 20%
- Correct . check: 20%
- Correct validation logic: 20%
- Proper output: 10%
"""

# Input data
email = "  User.Name@Example.COM  "

# Your code here
