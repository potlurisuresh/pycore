"""
Advanced Assignment 4: Customer Feedback Cleaner

Scenario:
Build an NLP preprocessing pipeline that cleans customer feedback, normalizes text,
detects sentiment indicators, extracts key entities, and generates content analytics.

Input:
- feedback_batch: Multi-line customer reviews
  "LOVE the product!!! Best purchase ever :) highly recommend!!!
   terrible quality... won't buy again :(   very disappointed
   ok product, nothing special    decent price tho
   AMAZING SERVICE!!! thx so much <3 will return
   bad experience with delivery... product itself was okay
   great value!!! super fast shipping :D very satisfied
   meh... not worth the $$$   overpriced"

Tasks:
1. Clean each review:
   - Remove excessive punctuation (!!!, ..., ???)
   - Normalize whitespace (strip, single spaces)
   - Standardize abbreviations:
     thx -> thanks, tho -> though, w/ -> with
   - Remove emoticons: :), :(, :D, <3
   - Convert to lowercase for analysis
2. Sentiment detection using keyword matching:
   - Positive: love, amazing, great, best, highly, excellent, satisfied
   - Negative: terrible, bad, won't, disappointed, overpriced, meh
   - Neutral: ok, okay, decent, nothing, special
3. Extract entities:
   - Product mentions (product, quality, value, price)
   - Service mentions (service, delivery, shipping)
   - Action indicators (recommend, buy, return)
4. Calculate review metrics:
   - Word count distribution
   - Sentiment score: (positive_words - negative_words)
   - Intensity indicators (ALL CAPS words, multiple punctuation)
   - Engagement markers (will return, recommend, won't buy)
5. Generate comprehensive content analytics report with recommendations

Expected Output:
Customer Feedback Analytics Report
====================================

Processing Summary:
Total Reviews: 7
Total Words Processed: 72
Average Words per Review: 10.3

Sentiment Analysis:
POSITIVE Reviews: 3 (42.9%)
  - "love the product best purchase ever highly recommend"
  - "amazing service thanks so much will return"
  - "great value super fast shipping very satisfied"

NEGATIVE Reviews: 3 (42.9%)
  - "terrible quality wont buy again very disappointed"
  - "bad experience with delivery product itself was okay"
  - "meh not worth the overpriced"

NEUTRAL Reviews: 1 (14.3%)
  - "ok product nothing special decent price though"

Sentiment Intensity:
High Positive: 2 reviews (multiple positive words + CAPS)
High Negative: 2 reviews (strong negative words)
Mixed Sentiment: 1 reviews (both positive and negative)

Entity Extraction:
Product Mentions: 5 occurrences
  - Reviews discussing: quality, product, value, price
Service Mentions: 3 occurrences
  - Reviews discussing: service, delivery, shipping
Action Indicators: 5 occurrences
  - Positive actions: recommend, will return (2)
  - Negative actions: wont buy, not worth (3)

Key Insights:
- Sentiment split: 42.9% positive vs 42.9% negative
- Service reviews highly positive (amazing, great, fast)
- Product quality concerns in negative reviews
- Delivery issues mentioned: 1 time
- Price sensitivity: 2 mentions (overpriced, decent price)
- Strong engagement: "will return", "highly recommend"

Cleaned Feedback (NLP Ready):
1. "love the product best purchase ever highly recommend" (POSITIVE)
2. "terrible quality wont buy again very disappointed" (NEGATIVE)
3. "ok product nothing special decent price though" (NEUTRAL)
4. "amazing service thanks so much will return" (POSITIVE)
5. "bad experience with delivery product itself was okay" (MIXED)
6. "great value super fast shipping very satisfied" (POSITIVE)
7. "meh not worth the overpriced" (NEGATIVE)

Recommendations:
- Address product quality issues (mentioned in negative reviews)
- Leverage strong service feedback for marketing
- Monitor price perception (overpriced mentions)
- Investigate delivery experience (1 complaint)
- Highlight fast shipping in promotions

Hints:
- Use replace() for abbreviations and emoticons
- Strip excessive punctuation with loops/regex
- Match keywords using 'in' operator
- Count occurrences across all reviews
- Track patterns in parallel lists

Rubric:
- Text cleaning accuracy: 20%
- Sentiment detection: 20%
- Entity extraction: 20%
- Metrics calculation: 20%
- Actionable insights: 20%
"""

# Input data
feedback_batch = """LOVE the product!!! Best purchase ever :) highly recommend!!!
terrible quality... won't buy again :(   very disappointed
ok product, nothing special    decent price tho
AMAZING SERVICE!!! thx so much <3 will return
bad experience with delivery... product itself was okay
great value!!! super fast shipping :D very satisfied
meh... not worth the $$$   overpriced"""

# Your code here
