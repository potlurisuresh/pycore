"""
Advanced Solution 4: Customer Feedback Cleaner (Concise)
"""

# Input data
feedback_batch = """LOVE the product!!! Best purchase ever :) highly recommend!!!
terrible quality... won't buy again :(   very disappointed
ok product, nothing special    decent price tho
AMAZING SERVICE!!! thx so much <3 will return
bad experience with delivery... product itself was okay
great value!!! super fast shipping :D very satisfied
meh... not worth the $$$   overpriced"""

feedbacks = [line.strip() for line in feedback_batch.strip().splitlines() if line.strip()]

replacements = {
    "!!!": "!",
    "...": ".",
    "$$$": "",
    "thx": "thanks",
    "tho": "though",
    ":)": "",
    ":(": "",
    ":D": "",
    "<3": "",
}

positive_words = {"love", "amazing", "great", "best", "highly", "satisfied", "recommend", "super", "fast"}
negative_words = {"terrible", "bad", "won't", "wont", "disappointed", "overpriced", "meh", "not worth"}
neutral_words = {"ok", "okay", "decent", "nothing"}

product_keywords = {"product", "quality", "value", "price"}
service_keywords = {"service", "delivery", "shipping"}

cleaned_feedbacks = []
sentiments = []
total_words = 0
product_mentions = 0
service_mentions = 0

for feedback in feedbacks:
    cleaned = feedback
    for k, v in replacements.items():
        cleaned = cleaned.replace(k, v)
    cleaned = " ".join(cleaned.split()).strip().lower()
    cleaned_feedbacks.append(cleaned)

    words = cleaned.split()
    total_words += len(words)

    pos = sum(1 for w in positive_words if w in cleaned)
    neg = sum(1 for w in negative_words if w in cleaned)
    if pos and not neg:
        sentiment = "POSITIVE"
    elif neg and not pos:
        sentiment = "NEGATIVE"
    elif pos and neg:
        sentiment = "MIXED"
    elif any(w in cleaned for w in neutral_words):
        sentiment = "NEUTRAL"
    else:
        sentiment = "NEUTRAL"
    sentiments.append(sentiment)

    if any(k in cleaned for k in product_keywords):
        product_mentions += 1
    if any(k in cleaned for k in service_keywords):
        service_mentions += 1

sent_counts = {s: sentiments.count(s) for s in set(sentiments)}

print("Customer Feedback Analytics")
print("=" * 48)
print(f"Reviews: {len(feedbacks)} | Total Words: {total_words} | Avg: {total_words/len(feedbacks):.1f}")

print("\nSentiment Counts:")
for s in ["POSITIVE", "NEGATIVE", "NEUTRAL", "MIXED"]:
    if s in sent_counts:
        print(f"- {s}: {sent_counts[s]}")

print("\nEntities:")
print(f"- Product mentions: {product_mentions}")
print(f"- Service mentions: {service_mentions}")

print("\nCleaned Samples:")
for i, text in enumerate(cleaned_feedbacks, 1):
    print(f"{i}. {text} ({sentiments[i-1]})")

print("\nRecommendations:")
if product_mentions:
    print("- Address product-related issues highlighted in feedback")
if service_mentions:
    print("- Leverage positive service mentions in messaging")
if sent_counts.get("NEGATIVE", 0) > 0:
    print("- Review negative feedback themes for remediation")
