"""
Mini Project 2: Contact Management System
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, lists
- P1.1.3: String methods (split, lower), f-strings
- P1.1.4: Tuples, dictionaries, sets

Description:
Store and organize contacts, search by name, and group by organization.
"""

# Contact database (tuples: name, phone, email, organization)
contacts = [
    ("Alice Johnson", "555-0101", "alice@techcorp.com", "TechCorp"),
    ("Bob Smith", "555-0102", "bob@techcorp.com", "TechCorp"),
    ("Carol White", "555-0103", "carol@designco.com", "DesignCo"),
    ("David Brown", "555-0104", "david@techcorp.com", "TechCorp"),
    ("Eve Davis", "555-0105", "eve@consulting.com", "Consulting"),
]

print("=" * 60)
print("CONTACT MANAGEMENT SYSTEM")
print("=" * 60)

# Step 1: Display all contacts
print("\nAll Contacts:")
print("-" * 60)
for contact in contacts:
    name, phone, email, org = contact  # Tuple unpacking
    print(f"{name:15s} | {phone:10s} | {email:25s} | {org}")

# Step 2: Count contacts by organization
org_counts = {}
for contact in contacts:
    org = contact[3]  # Organization is 4th element
    if org in org_counts:
        org_counts[org] += 1
    else:
        org_counts[org] = 1

print("\nContacts by Organization:")
for org, count in org_counts.items():
    print(f"  {org:15s}: {count} contacts")

# Step 3: Get unique organizations using set
unique_orgs = set()
for contact in contacts:
    unique_orgs.add(contact[3])

print(f"\nUnique Organizations: {len(unique_orgs)}")
print(f"Organizations: {unique_orgs}")

# Step 4: Search for contacts (example: search for "alice")
search_term = "alice"
print(f"\nSearching for '{search_term}':")
found_contacts = []
for contact in contacts:
    name, phone, email, org = contact
    if search_term.lower() in name.lower():
        found_contacts.append(contact)

if found_contacts:
    for contact in found_contacts:
        name, phone, email, org = contact
        print(f"  {name} - {email}")
else:
    print("  No contacts found")

# Step 5: Filter TechCorp contacts
print("\nTechCorp Contacts:")
techcorp_contacts = []
for contact in contacts:
    if contact[3] == "TechCorp":
        techcorp_contacts.append(contact)

for contact in techcorp_contacts:
    name = contact[0]
    email = contact[2]
    print(f"  {name} - {email}")

print(f"\nTotal TechCorp employees: {len(techcorp_contacts)}")
print("=" * 60)
