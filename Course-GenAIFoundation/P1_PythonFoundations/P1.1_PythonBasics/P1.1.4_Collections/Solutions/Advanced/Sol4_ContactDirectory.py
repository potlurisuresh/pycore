"""
Advanced Solution 4: Contact Directory
"""

# Input data
contacts_data = """1,Alice CEO,555-1111,alice@company.com
2,Bob Manager,555-2222,bob@company.com
3,Carol Vendor,555-3333,carol@vendor.com
1,David CTO,555-4444,david@company.com
2,Eve Lead,555-2222,eve@company.com"""

# Parse into tuples
contacts = []
for line in contacts_data.split('\n'):
    priority, name, phone, email = [p.strip() for p in line.split(',')]
    contacts.append((int(priority), name, phone, email))

# Sort by priority then name
sorted_contacts = sorted(contacts, key=lambda x: (x[0], x[1]))

# Group by domain and priority
domain_priority = {}
for priority, name, phone, email in contacts:
    domain = email.split('@')[1]
    key = (domain, priority)
    if key not in domain_priority:
        domain_priority[key] = []
    domain_priority[key].append(name)

# Find duplicate phones
phone_map = {}
for priority, name, phone, email in contacts:
    if phone not in phone_map:
        phone_map[phone] = []
    phone_map[phone].append(name)

duplicates = {phone: names for phone, names in phone_map.items() if len(names) > 1}

print("Sorted Contacts (by priority, then name):")
for priority, name, phone, email in sorted_contacts:
    p_label = ['VIP', 'Regular', 'Other'][priority - 1]
    print(f"[{p_label}] {name} | {phone} | {email}")

print("\nBy Domain and Priority:")
for key, names in sorted(domain_priority.items()):
    print(f"{key}: {names}")

print("\nDuplicate Phone Numbers:")
for phone, names in duplicates.items():
    print(f"{phone}: {names}")
