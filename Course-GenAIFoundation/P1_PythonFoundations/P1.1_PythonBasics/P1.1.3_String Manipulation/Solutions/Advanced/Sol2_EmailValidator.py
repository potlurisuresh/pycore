"""
Advanced Solution 2: Email Validator (Concise)
"""
import re

# Input data
email_database = """john.doe@company.com, admin@test.org, user+tag@site.co.uk
suspicious123@temp-mail.com, contact@company.com, admin@company.com
invalid@, test@localhost, marketing@company.com"""

emails = [e.strip().lower() for e in email_database.replace("\n", ", ").split(", ") if e.strip()]
pattern = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
suspicious_keywords = {"temp", "mail"}

valid_emails = [e for e in emails if re.match(pattern, e)]
invalid_emails = [e for e in emails if e not in valid_emails]
domains = [e.split("@")[1] for e in valid_emails]

domain_counts = {}
for d in domains:
    domain_counts[d] = domain_counts.get(d, 0) + 1

def trust_score(email):
    domain = email.split("@")[1]
    score = 0
    if domain.endswith((".com", ".org", ".co.uk")):
        score += 40
    if not any(k in domain for k in suspicious_keywords):
        score += 25
    if "+" not in email:
        score += 20
    if domain_counts.get(domain, 0) > 1:
        score += 15
    return score

scores = {e: trust_score(e) for e in valid_emails}
high_trust = [e for e, s in scores.items() if s >= 70]
low_trust = [e for e, s in scores.items() if s < 70]

suspicious_emails = [e for e in valid_emails if any(k in e.split("@")[1] for k in suspicious_keywords)]
aliased_emails = [e for e in valid_emails if "+" in e]

print("Email Intelligence Report")
print("=" * 48)
print(f"Total Emails: {len(emails)} | Valid: {len(valid_emails)} | Invalid: {len(invalid_emails)}")

print("\nDomain Summary:")
for domain, count in sorted(domain_counts.items(), key=lambda x: (-x[1], x[0])):
    tag = "SUSPICIOUS" if any(k in domain for k in suspicious_keywords) else "CORPORATE"
    print(f"- {domain}: {count} ({tag})")

print("\nRisk Assessment:")
print(f"HIGH TRUST (70+): {len(high_trust)}")
print(f"LOW TRUST (<70): {len(low_trust)}")

print("\nFlags:")
for e in suspicious_emails:
    print(f"- Suspicious domain: {e}")
for e in aliased_emails:
    print(f"- Aliased email: {e}")

print("\nRecommendations:")
if suspicious_emails:
    print("- Review disposable/temporary domains")
if aliased_emails:
    print("- Monitor alias usage for abuse")
if domain_counts:
    main_domain = max(domain_counts, key=domain_counts.get)
    print(f"- Primary organization domain: {main_domain}")
