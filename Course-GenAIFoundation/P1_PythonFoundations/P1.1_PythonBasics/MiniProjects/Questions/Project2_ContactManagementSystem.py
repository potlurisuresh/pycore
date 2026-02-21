"""
Mini Project 2: Contact Management System
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, lists
- P1.1.3: String methods (split, lower), f-strings
- P1.1.4: Tuples, dictionaries, sets

Description:
Build a contact management system that:
1. Stores contacts as tuples (name, phone, email, organization)
2. Displays all contacts in formatted table
3. Counts contacts by organization
4. Gets unique organizations using sets
5. Searches contacts by name
6. Filters contacts by organization

Expected Output:
============================================================
CONTACT MANAGEMENT SYSTEM
============================================================

All Contacts:
------------------------------------------------------------
Alice Johnson   | 555-0101   | alice@techcorp.com        | TechCorp
Bob Smith       | 555-0102   | bob@techcorp.com          | TechCorp
...

Contacts by Organization:
  TechCorp       : 3 contacts
  DesignCo       : 1 contacts
  ...

Unique Organizations: 3
Organizations: {'TechCorp', 'DesignCo', 'Consulting'}

Searching for 'alice':
  Alice Johnson - alice@techcorp.com

TechCorp Contacts:
  Alice Johnson - alice@techcorp.com
  Bob Smith - bob@techcorp.com
  ...

Total TechCorp employees: 3
============================================================
"""

# Contact database - DO NOT MODIFY
# Each contact is a tuple: (name, phone, email, organization)
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

# TODO: Step 1 - Display all contacts
# Loop through contacts list
# For each contact, unpack the tuple into: name, phone, email, org
# Print in formatted way using f-string

print("\nAll Contacts:")
print("-" * 60)
# YOUR CODE HERE


# TODO: Step 2 - Count contacts by organization
# Create an empty dictionary called 'org_counts'
# Loop through contacts
# For each contact, get the organization (4th element, index 3)
# Count how many times each organization appears

org_counts = {}
# YOUR CODE HERE


print("\nContacts by Organization:")
for org, count in org_counts.items():
    print(f"  {org:15s}: {count} contacts")

# TODO: Step 3 - Get unique organizations using set
# Create an empty set called 'unique_orgs'
# Loop through contacts and add each organization to the set

unique_orgs = set()
# YOUR CODE HERE


print(f"\nUnique Organizations: {len(unique_orgs)}")
print(f"Organizations: {unique_orgs}")

# TODO: Step 4 - Search for contacts
# Search term is "alice"
# Create an empty list 'found_contacts'
# Loop through contacts
# Unpack each contact tuple
# Check if search_term (lowercase) is in name (lowercase)
# If found, add to found_contacts list

search_term = "alice"
print(f"\nSearching for '{search_term}':")
found_contacts = []
# YOUR CODE HERE


if found_contacts:
    for contact in found_contacts:
        name, phone, email, org = contact
        print(f"  {name} - {email}")
else:
    print("  No contacts found")

# TODO: Step 5 - Filter TechCorp contacts
# Create an empty list 'techcorp_contacts'
# Loop through contacts
# If organization is "TechCorp", add to list

print("\nTechCorp Contacts:")
techcorp_contacts = []
# YOUR CODE HERE


for contact in techcorp_contacts:
    name = contact[0]
    email = contact[2]
    print(f"  {name} - {email}")

print(f"\nTotal TechCorp employees: {len(techcorp_contacts)}")
print("=" * 60)
