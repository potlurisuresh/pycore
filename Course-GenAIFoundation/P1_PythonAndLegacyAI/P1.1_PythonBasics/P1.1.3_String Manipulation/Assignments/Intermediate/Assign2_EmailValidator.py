"""
Intermediate Assignment 2: Email Validator

Scenario:
Validate multiple email addresses using regex and extract domain statistics.

Input:
- email_list: "user@example.com, admin@test.org, invalid@, contact@site.co.uk"

Tasks:
1. Split email_list by ',' and clean each (strip whitespace, lowercase)
2. Validate each email using regex: r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
3. For valid emails, extract domain (part after @)
4. Count how many emails per domain
5. Print validation results and domain statistics

Expected Output:
Email Validation Results
------------------------
Total: 4
Valid: 3
Invalid: 1

Domain Statistics:
example.com: 1 email(s)
test.org: 1 email(s)
site.co.uk: 1 email(s)

Valid Emails:
- user@example.com
- admin@test.org
- contact@site.co.uk

Hints:
- Use import re
- Use split(',') and strip()
- Use re.match() for validation
- Use split('@') to extract domain
- Track domains in parallel lists

Rubric:
- Correct parsing and cleaning: 20%
- Correct regex validation: 30%
- Correct domain extraction: 25%
- Correct statistics: 15%
- Proper output: 10%
"""

# Input data
email_list = "user@example.com, admin@test.org, invalid@, contact@site.co.uk"

# Your code here
