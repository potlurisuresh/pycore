"""
Advanced Solution 2: Email Validator
"""
import re

# Input data
email_database = """john.doe@company.com, admin@test.org, user+tag@site.co.uk
suspicious123@temp-mail.com, contact@company.com, admin@company.com
invalid@, test@localhost, marketing@company.com"""

# Parse emails
all_emails = email_database.replace("\n", ", ").split(", ")
all_emails = [e.strip() for e in all_emails if e.strip()]

# Regex for validation
pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"

# Validate emails
valid_emails = []
invalid_emails = []
domains = []
suspicious_keywords = ["temp", "mail"]

for email in all_emails:
    email_clean = email.strip().lower()
    if re.match(pattern, email_clean):
        valid_emails.append(email_clean)
        domain = email_clean.split("@")[1]
        domains.append(domain)
    else:
        invalid_emails.append(email)

# Domain statistics
unique_domains = []
domain_counts = []

for domain in domains:
    if domain not in unique_domains:
        unique_domains.append(domain)
        domain_counts.append(domains.count(domain))

# Calculate trust scores
trust_scores = []
for email in valid_emails:
    score = 0
    domain = email.split("@")[1]
    
    # Corporate domain
    if domain.endswith(".com") or domain.endswith(".org"):
        score += 40
    
    # No suspicious keywords
    has_suspicious = any(kw in domain for kw in suspicious_keywords)
    if not has_suspicious:
        score += 30
    
    # No aliasing
    if "+" not in email:
        score += 20
    
    # Multiple users from same domain
    if domains.count(domain) > 1:
        score += 10
    
    trust_scores.append(score)

# Categorize by trust
high_trust = []
low_trust = []

for i in range(len(valid_emails)):
    if trust_scores[i] >= 70:
        high_trust.append(valid_emails[i])
    else:
        low_trust.append(valid_emails[i])

# Detect patterns
suspicious_emails = []
aliased_emails = []

for email in valid_emails:
    domain = email.split("@")[1]
    
    # Check suspicious domains
    if any(kw in domain for kw in suspicious_keywords):
        suspicious_emails.append(email)
    
    # Check aliasing
    if "+" in email:
        aliased_emails.append(email)

# Print report
print("Email Intelligence Report")
print("=" * 50)
print()

print("Validation Summary:")
print(f"Total Emails: {len(all_emails)}")
print(f"Valid Format: {len(valid_emails)}")
print(f"Invalid Format: {len(invalid_emails)}")
print()

print("Domain Analysis:")
for i in range(len(unique_domains)):
    domain = unique_domains[i]
    count = domain_counts[i]
    percentage = count * 100.0 / len(valid_emails)
    
    print(f"{domain}: {count} emails ({percentage:.1f}% of valid)")
    
    # Determine trust level
    if count > 1 and not any(kw in domain for kw in suspicious_keywords):
        trust_level = "HIGH (corporate, multiple users)"
    elif any(kw in domain for kw in suspicious_keywords):
        trust_level = "LOW (suspicious keywords)"
    else:
        trust_level = "MEDIUM"
    
    print(f"  Trust Level: {trust_level}")
print()

print("Risk Assessment:")
print(f"HIGH TRUST (70-100): {len(high_trust)} emails")
print(f"LOW TRUST (0-69): {len(low_trust)} emails")
print()

print("Suspicious Patterns Detected:")
if len(suspicious_emails) > 0:
    for email in suspicious_emails:
        print(f"WARNING: Temporary email service: {email}")
if len(aliased_emails) > 0:
    for email in aliased_emails:
        print(f"WARNING: Email aliasing: {email}")
print()

print("Top Domains:")
for i in range(min(3, len(unique_domains))):
    max_count = max(domain_counts)
    max_index = domain_counts.index(max_count)
    domain = unique_domains[max_index]
    
    print(f"{i + 1}. {domain} - {max_count} emails")
    domain_counts[max_index] = -1
print()

print("Recommendations:")
if len(suspicious_emails) > 0:
    print("- Review temporary/suspicious email services")
if len(aliased_emails) > 0:
    print("- Monitor aliased emails for abuse")
# Find most popular legitimate domain
max_count = 0
main_domain = ""
for i in range(len(unique_domains)):
    if domains.count(unique_domains[i]) > max_count:
        if not any(kw in unique_domains[i] for kw in suspicious_keywords):
            max_count = domains.count(unique_domains[i])
            main_domain = unique_domains[i]
if main_domain:
    print(f"- {main_domain} shows legitimate organization pattern")
