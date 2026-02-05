"""
Intermediate Solution 4: Contact Directory
"""

# Input data
contacts_data = """John Doe, 555-1234, john@company.com
Alice Smith, 555-2345, alice@email.com
Bob Jones, 555-3456, bob@company.com
Carol White, 555-4567, carol@email.com"""

# Parse into list of tuples
contacts = []
for line in contacts_data.split('\n'):
    parts = [p.strip() for p in line.split(',')]
    contact = (parts[0], parts[1], parts[2])  # Tuple
    contacts.append(contact)

# Sort by name
sorted_by_name = sorted(contacts, key=lambda x: x[0])

# Sort by phone
sorted_by_phone = sorted(contacts, key=lambda x: x[1])

# Find company.com contacts
company_contacts = [c for c in contacts if '@company.com' in c[2]]

print("Original contacts:")
for name, phone, email in contacts:
    print(f"{name} | {phone} | {email}")

print("\nSorted by name:")
for name, phone, email in sorted_by_name:
    print(f"{name} | {phone} | {email}")

print("\nCompany contacts:")
for name, phone, email in company_contacts:
    print(f"{name} | {phone} | {email}")
