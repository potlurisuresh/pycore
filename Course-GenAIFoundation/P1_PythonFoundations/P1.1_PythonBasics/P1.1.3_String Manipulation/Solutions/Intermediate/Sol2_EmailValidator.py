"""
Intermediate Solution 2: Email Validator
"""
import re

# Input data
email_list = "john.doe@company.com, admin@test.org, invalid-email, user@site.co.uk"

# Parse emails
emails = email_list.split(", ")

# Regex pattern for email validation
pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"

# Initialize lists
valid_emails = []
invalid_emails = []
domains = []

# Validate each email
for email in emails:
    email_clean = email.strip().lower()
    if re.match(pattern, email_clean):
        valid_emails.append(email_clean)
        # Extract domain
        domain = email_clean.split("@")[1]
        domains.append(domain)
    else:
        invalid_emails.append(email)

# Count domain occurrences
domain_counts = []
domain_names = []
for domain in domains:
    if domain not in domain_names:
        domain_names.append(domain)
        count = domains.count(domain)
        domain_counts.append(count)

# Print formatted output
print("Email Validation Report")
print("=" * 30)
print(f"Total Emails: {len(emails)}")
print(f"Valid: {len(valid_emails)}")
print(f"Invalid: {len(invalid_emails)}")
print()
print("Valid Emails:")
for email in valid_emails:
    print(f"  - {email}")
print()
print("Domain Statistics:")
for i in range(len(domain_names)):
    print(f"  {domain_names[i]}: {domain_counts[i]} email(s)")
