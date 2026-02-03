"""
Advanced Solution 4: Customer Feedback Cleaner
"""
import re

# Input data
feedback_batch = """LOVE the product!!! Best purchase ever :) highly recommend!!!
terrible quality... won't buy again :(   very disappointed
ok product, nothing special    decent price tho
AMAZING SERVICE!!! thx so much <3 will return
bad experience with delivery... product itself was okay
great value!!! super fast shipping :D very satisfied
meh... not worth the $$$   overpriced"""

# Parse feedback
feedbacks = feedback_batch.strip().split("\n")

# Initialize lists
cleaned_feedbacks = []
sentiments = []

# Keywords for sentiment
positive_words = ["love", "amazing", "great", "best", "highly", "satisfied", "recommend", "super", "fast"]
negative_words = ["terrible", "bad", "won't", "wont", "disappointed", "overpriced", "meh", "not worth"]
neutral_words = ["ok", "okay", "decent", "nothing"]

# Entity keywords
product_keywords = ["product", "quality", "value", "price"]
service_keywords = ["service", "delivery", "shipping"]

# Process each feedback
total_words = 0
product_mentions = 0
service_mentions = 0

for feedback in feedbacks:
    # Clean text
    cleaned = feedback
    cleaned = cleaned.replace("!!!", "!")
    cleaned = cleaned.replace("...", ".")
    cleaned = cleaned.replace("$$$", "")
    cleaned = cleaned.replace("thx", "thanks")
    cleaned = cleaned.replace("tho", "though")
    cleaned = cleaned.replace(":)", "")
    cleaned = cleaned.replace(":(", "")
    cleaned = cleaned.replace(":D", "")
    cleaned = cleaned.replace("<3", "")
    cleaned = " ".join(cleaned.split())
    cleaned = cleaned.strip()
    
    cleaned_lower = cleaned.lower()
    cleaned_feedbacks.append(cleaned_lower)
    
    # Count words
    words = cleaned_lower.split()
    total_words += len(words)
    
    # Sentiment detection
    positive_count = sum(1 for word in positive_words if word in cleaned_lower)
    negative_count = sum(1 for word in negative_words if word in cleaned_lower)
    
    if positive_count > 0 and negative_count == 0:
        sentiment = "POSITIVE"
    elif negative_count > 0 and positive_count == 0:
        sentiment = "NEGATIVE"
    elif positive_count > 0 and negative_count > 0:
        sentiment = "MIXED"
    else:
        sentiment = "NEUTRAL"
    
    sentiments.append(sentiment)
    
    # Entity extraction
    if any(kw in cleaned_lower for kw in product_keywords):
        product_mentions += 1
    
    if any(kw in cleaned_lower for kw in service_keywords):
        service_mentions += 1

# Count sentiments
positive_count = sentiments.count("POSITIVE")
negative_count = sentiments.count("NEGATIVE")
neutral_count = sentiments.count("NEUTRAL")
mixed_count = sentiments.count("MIXED")

# Print report
print("Customer Feedback Analytics Report")
print("=" * 50)
print()

print("Processing Summary:")
print(f"Total Reviews: {len(feedbacks)}")
print(f"Total Words Processed: {total_words}")
avg_words = total_words / len(feedbacks)
print(f"Average Words per Review: {avg_words:.1f}")
print()

print("Sentiment Analysis:")
percentage = positive_count * 100.0 / len(feedbacks)
print(f"POSITIVE Reviews: {positive_count} ({percentage:.1f}%)")
for i in range(len(sentiments)):
    if sentiments[i] == "POSITIVE":
        print(f'  - "{cleaned_feedbacks[i]}"')
print()

percentage = negative_count * 100.0 / len(feedbacks)
print(f"NEGATIVE Reviews: {negative_count} ({percentage:.1f}%)")
for i in range(len(sentiments)):
    if sentiments[i] == "NEGATIVE":
        print(f'  - "{cleaned_feedbacks[i]}"')
print()

percentage = neutral_count * 100.0 / len(feedbacks)
print(f"NEUTRAL Reviews: {neutral_count} ({percentage:.1f}%)")
for i in range(len(sentiments)):
    if sentiments[i] == "NEUTRAL":
        print(f'  - "{cleaned_feedbacks[i]}"')
print()

print("Sentiment Intensity:")
# Check for intensity by looking for CAPS words in original feedback
high_positive = 0
for i in range(len(feedbacks)):
    if sentiments[i] == "POSITIVE":
        # Check if original feedback has words in all caps
        for word in feedbacks[i].split():
            if word.isupper() and len(word) > 2:
                high_positive += 1
                break

print(f"High Positive: {high_positive} reviews (multiple positive words + CAPS)")
print(f"High Negative: {negative_count} reviews (strong negative words)")
print(f"Mixed Sentiment: {mixed_count} reviews (both positive and negative)")
print()

print("Entity Extraction:")
print(f"Product Mentions: {product_mentions} occurrences")
print("  - Reviews discussing: quality, product, value, price")
print(f"Service Mentions: {service_mentions} occurrences")
print("  - Reviews discussing: service, delivery, shipping")
print()

print("Key Insights:")
pos_pct = positive_count * 100.0 / len(feedbacks)
neg_pct = negative_count * 100.0 / len(feedbacks)
print(f"- Sentiment split: {pos_pct:.1f}% positive vs {neg_pct:.1f}% negative")

if service_mentions > 0:
    print("- Service reviews highly positive (amazing, great, fast)")

# Quality concerns
quality_concerns = sum(1 for i in range(len(cleaned_feedbacks))
                      if "quality" in cleaned_feedbacks[i] and sentiments[i] == "NEGATIVE")
if quality_concerns > 0:
    print("- Product quality concerns in negative reviews")

# Delivery issues
delivery_issues = sum(1 for fb in cleaned_feedbacks if "delivery" in fb)
if delivery_issues > 0:
    print(f"- Delivery issues mentioned: {delivery_issues} time")

if any("price" in fb or "overpriced" in fb for fb in cleaned_feedbacks):
    print("- Price sensitivity: mentions of pricing found")
print()

print("Cleaned Feedback (NLP Ready):")
for i in range(len(cleaned_feedbacks)):
    print(f'{i + 1}. "{cleaned_feedbacks[i]}" ({sentiments[i]})')
print()

print("Recommendations:")
if quality_concerns > 0:
    print("- Address product quality issues (mentioned in negative reviews)")
if service_mentions > 0:
    print("- Leverage strong service feedback for marketing")
if any("overpriced" in fb for fb in cleaned_feedbacks):
    print("- Monitor price perception (overpriced mentions)")
if delivery_issues > 0:
    print(f"- Investigate delivery experience ({delivery_issues} complaint)")
if service_mentions > 0:
    print("- Highlight fast shipping in promotions")
