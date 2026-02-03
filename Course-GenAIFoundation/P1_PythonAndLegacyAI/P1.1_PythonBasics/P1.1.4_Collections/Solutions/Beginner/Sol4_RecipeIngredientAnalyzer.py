"""
Beginner Solution 4: Contact Directory
"""

# Input data
contact_str = "John Doe, 555-1234, john@email.com"

# Parse and create tuple
parts = [p.strip() for p in contact_str.split(',')]
contact = (parts[0], parts[1], parts[2])  # Tuple is immutable

# Unpack tuple
name, phone, email = contact

print(f"Contact tuple: {contact}")
print(f"\nUnpacked values:")
print(f"Name: {name}")
print(f"Phone: {phone}")
print(f"Email: {email}")
