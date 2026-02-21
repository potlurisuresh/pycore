"""
Beginner Solution 2: Email Validator
"""

# Input data
email = "  John.Doe@EXAMPLE.COM  "

# Clean the email
cleaned_email = email.strip()  # Remove spaces
cleaned_email = cleaned_email.lower()  # Convert to lowercase

# Extract username and domain
parts = cleaned_email.split("@")
username = parts[0]
domain = parts[1]

# Print formatted output
print("Email Validator")
print("=" * 20)
print(f"Original: {email}")
print(f"Cleaned: {cleaned_email}")
print(f"Username: {username}")
print(f"Domain: {domain}")
