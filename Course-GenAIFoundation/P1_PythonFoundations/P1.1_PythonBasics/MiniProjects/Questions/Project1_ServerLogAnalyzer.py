"""
Mini Project 1: Server Log Analyzer
Level: Intermediate

Concepts Used:
- P1.1.2: Loops, conditions, lists
- P1.1.3: String methods (split, strip), f-strings
- P1.1.4: Dictionaries, lists

Description:
You need to build a log analyzer that reads server logs and provides insights.
The program should:
1. Parse each log entry into date, time, level, and message
2. Count how many logs exist for each severity level (INFO, WARNING, ERROR, CRITICAL)
3. Find recurring error messages
4. Calculate a severity score based on error levels
5. Display a formatted report

Expected Output:
==================================================
SERVER LOG ANALYZER
==================================================

Total logs processed: 10

Log Level Breakdown:
  CRITICAL  : 1
  ERROR     : 4
  WARNING   : 2
  INFO      : 3

Error Messages:
  [3x] Database connection failed
  [1x] File not found

Severity Score: 34
Status: CRITICAL - Needs attention!
==================================================
"""

# Sample log data - DO NOT MODIFY
log_data = """2026-02-03 10:15:23 INFO Server started
2026-02-03 10:16:45 ERROR Database connection failed
2026-02-03 10:17:12 WARNING Memory usage high
2026-02-03 10:18:33 ERROR Database connection failed
2026-02-03 10:19:01 INFO User logged in
2026-02-03 10:20:15 ERROR File not found
2026-02-03 10:21:48 WARNING Disk space low
2026-02-03 10:22:30 INFO User logged in
2026-02-03 10:23:17 ERROR Database connection failed
2026-02-03 10:24:55 CRITICAL System memory exhausted"""

print("=" * 50)
print("SERVER LOG ANALYZER")
print("=" * 50)

# TODO: Step 1 - Parse logs into list of dictionaries
# Create an empty list called 'logs'
# Loop through each line in log_data
# Split each line by space (limit to 4 parts: date, time, level, message)
# Create a dictionary with keys: 'date', 'time', 'level', 'message'
# Append to logs list

logs = []
# YOUR CODE HERE


print(f"\nTotal logs processed: {len(logs)}")

# TODO: Step 2 - Count logs by level
# Create an empty dictionary called 'level_counts'
# Loop through each log in logs list
# For each log, increment the count for that level
# If level doesn't exist in dictionary, initialize it to 1

level_counts = {}
# YOUR CODE HERE


# TODO: Step 3 - Display level breakdown
print("\nLog Level Breakdown:")
for level in ['CRITICAL', 'ERROR', 'WARNING', 'INFO']:
    count = level_counts.get(level, 0)
    print(f"  {level:10s}: {count}")

# TODO: Step 4 - Find most common errors
# Create an empty dictionary called 'error_messages'
# Loop through logs and find only ERROR level entries
# Count how many times each error message appears

error_messages = {}
# YOUR CODE HERE


print("\nError Messages:")
for msg, count in error_messages.items():
    print(f"  [{count}x] {msg}")

# TODO: Step 5 - Calculate severity score
# Calculate: CRITICAL * 10 + ERROR * 5 + WARNING * 2
# Store in variable 'severity_score'

severity_score = 0
# YOUR CODE HERE


print(f"\nSeverity Score: {severity_score}")
if severity_score > 30:
    print("Status: CRITICAL - Needs attention!")
elif severity_score > 10:
    print("Status: WARNING - Monitor system")
else:
    print("Status: HEALTHY")

print("=" * 50)
