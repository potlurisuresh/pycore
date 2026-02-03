"""
Intermediate Solution 4: Customer Feedback Cleaner
"""

# Input data
feedback_batch = """Great product!!! thx for delivery :)
terrible quality... very disappointed :(
ok service, nothing special"""

# Parse feedback
feedbacks = feedback_batch.strip().split("\n")

# Initialize lists
cleaned_feedbacks = []
sentiments = []

# Keywords for sentiment
positive_words = ["great", "excellent", "amazing", "love", "best"]
negative_words = ["terrible", "bad", "disappointed", "worst", "poor"]

# Process each feedback
for feedback in feedbacks:
    # Clean text
    cleaned = feedback.replace("!!!", "!")
    cleaned = cleaned.replace("...", ".")
    cleaned = cleaned.replace("thx", "thanks")
    cleaned = cleaned.replace(":)", "")
    cleaned = cleaned.replace(":(", "")
    cleaned = cleaned.strip()
    cleaned_feedbacks.append(cleaned)
    
    # Detect sentiment
    feedback_lower = cleaned.lower()
    has_positive = False
    has_negative = False
    
    for word in positive_words:
        if word in feedback_lower:
            has_positive = True
            break
    
    for word in negative_words:
        if word in feedback_lower:
            has_negative = True
            break
    
    if has_positive and not has_negative:
        sentiments.append("POSITIVE")
    elif has_negative and not has_positive:
        sentiments.append("NEGATIVE")
    else:
        sentiments.append("NEUTRAL")

# Count sentiments
positive_count = sentiments.count("POSITIVE")
negative_count = sentiments.count("NEGATIVE")
neutral_count = sentiments.count("NEUTRAL")

# Print formatted output
print("Feedback Analysis Report")
print("=" * 30)
print(f"Total Feedbacks: {len(feedbacks)}")
print()
print("Sentiment Summary:")
print(f"  POSITIVE: {positive_count}")
print(f"  NEGATIVE: {negative_count}")
print(f"  NEUTRAL: {neutral_count}")
print()
print("Cleaned Feedbacks:")
for i in range(len(cleaned_feedbacks)):
    print(f"  [{sentiments[i]}] {cleaned_feedbacks[i]}")
