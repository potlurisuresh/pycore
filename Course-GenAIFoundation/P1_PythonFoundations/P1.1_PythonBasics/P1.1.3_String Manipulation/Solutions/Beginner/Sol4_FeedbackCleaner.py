"""
Beginner Solution 4: Customer Feedback Cleaner
"""

# Input data
feedback = "Great product!!! thx for the fast delivery :)"

# Clean the feedback
cleaned = feedback.replace("!!!", "!")  # Remove excessive exclamation
cleaned = cleaned.replace("thx", "thanks")  # Replace abbreviation
cleaned = cleaned.replace(":)", "")  # Remove emoticon
cleaned = cleaned.strip()  # Remove extra spaces

# Print formatted output
print("Feedback Cleaner")
print("=" * 20)
print(f"Original: {feedback}")
print(f"Cleaned: {cleaned}")
