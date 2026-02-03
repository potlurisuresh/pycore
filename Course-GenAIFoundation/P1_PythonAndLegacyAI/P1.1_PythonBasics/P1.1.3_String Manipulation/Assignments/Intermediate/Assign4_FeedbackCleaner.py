"""
Intermediate Assignment 4: Customer Feedback Cleaner

Scenario:
Clean multiple feedback entries, normalize text, and detect sentiment keywords.

Input:
- feedback_batch: "prod is gr8! svc was avg. | Quality is poor but price gud | gr8 prod, terrible svc"

Tasks:
1. Split feedback_batch by '|' to get individual feedbacks
2. For each, replace abbreviations: prod→product, gr8→great, svc→service, avg→average, gud→good
3. Count positive keywords: great, good, quality
4. Count negative keywords: poor, terrible, bad
5. Calculate overall sentiment for each feedback

Expected Output:
Feedback Analysis
-----------------
Total Feedbacks: 3

Feedback 1:
Original: prod is gr8! svc was avg.
Cleaned: product is great! service was average.
Sentiment: Positive (1 positive, 0 negative)

Feedback 2:
Original: Quality is poor but price gud
Cleaned: Quality is poor but price good
Sentiment: Neutral (2 positive, 1 negative)

Feedback 3:
Original: gr8 prod, terrible svc
Cleaned: great product, terrible service
Sentiment: Neutral (1 positive, 1 negative)

Summary:
Positive: 1
Neutral: 2
Negative: 0

Hints:
- Use split('|') and strip()
- Chain multiple replace() calls
- Use lower() before counting keywords
- Use 'in' to check keyword presence
- Compare counts for sentiment

Rubric:
- Correct parsing and cleaning: 25%
- Correct abbreviation replacement: 25%
- Correct keyword detection: 25%
- Correct sentiment logic: 15%
- Proper output: 10%
"""

# Input data
feedback_batch = "prod is gr8! svc was avg. | Quality is poor but price gud | gr8 prod, terrible svc"

# Your code here
