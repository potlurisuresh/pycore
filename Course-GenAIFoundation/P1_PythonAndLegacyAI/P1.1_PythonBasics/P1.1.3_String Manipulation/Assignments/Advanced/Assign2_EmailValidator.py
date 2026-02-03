"""
Advanced Assignment 2: Email Validator

Scenario:
Build an email intelligence system that validates emails using complex regex,
categorizes by domain type, detects suspicious patterns, and generates risk scores.

Input:
- email_database: Multi-line email data
  "john.doe@company.com, admin@test.org, user+tag@site.co.uk
   suspicious123@temp-mail.com, contact@company.com, admin@company.com
   invalid@, test@localhost, marketing@company.com"

Tasks:
1. Parse and clean all emails (strip, lowercase)
2. Validate using comprehensive regex: r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
3. Categorize domains:
   - Corporate (.com, .org, .co.uk)
   - Suspicious (contains 'temp', 'mail', digits in domain)
   - Local (localhost, no TLDs)
4. Extract domain statistics and find duplicates
5. Detect patterns:
   - Multiple users from same domain
   - Email aliasing (using + tags)
   - Suspicious naming patterns
6. Calculate trust score per email (0-100):
   - Corporate domain: +40
   - Valid TLD: +20
   - No suspicious keywords: +20
   - No aliasing: +10
   - Domain reputation (multiple users): +10
7. Generate comprehensive email intelligence report

Expected Output:
Email Intelligence Report
==========================

Validation Summary:
Total Emails: 9
Valid Format: 7
Invalid Format: 2

Domain Analysis:
company.com: 4 emails (57.1% of valid)
  - john.doe@company.com
  - contact@company.com
  - admin@company.com
  - marketing@company.com
  Trust Level: HIGH (corporate, multiple users)

test.org: 1 emails (14.3% of valid)
  - admin@test.org
  Trust Level: MEDIUM (corporate, single user)

site.co.uk: 1 emails (14.3% of valid)
  - user+tag@site.co.uk
  Trust Level: MEDIUM (aliasing detected)

temp-mail.com: 1 emails (14.3% of valid)
  - suspicious123@temp-mail.com
  Trust Level: LOW (suspicious keywords)

Risk Assessment:
HIGH TRUST (80-100): 4 emails
MEDIUM TRUST (50-79): 2 emails
LOW TRUST (0-49): 1 emails

Suspicious Patterns Detected:
WARNING: Temporary email service: temp-mail.com
WARNING: Email aliasing: user+tag@site.co.uk
WARNING: Numeric username: suspicious123

Top Domains:
1. company.com - 4 emails (Multiple user organization)
2. test.org - 1 emails
3. site.co.uk - 1 emails

Recommendations:
- Review emails from temp-mail.com (disposable service)
- Monitor aliased emails for abuse
- company.com shows legitimate organization pattern

Hints:
- Use complex regex patterns
- Parse domain carefully (split '@')
- Detect keywords with 'in' operator
- Score based on multiple criteria
- Track patterns in lists

Rubric:
- Correct validation: 15%
- Domain categorization: 20%
- Pattern detection: 25%
- Trust scoring: 20%
- Comprehensive report: 20%
"""

# Input data
email_database = """john.doe@company.com, admin@test.org, user+tag@site.co.uk
suspicious123@temp-mail.com, contact@company.com, admin@company.com
invalid@, test@localhost, marketing@company.com"""

# Your code here
