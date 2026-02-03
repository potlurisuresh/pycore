"""
Intermediate Assignment 1: Log Entry Parser

Scenario:
Parse multiple log entries, count entries by log level, and identify error patterns.

Input:
- log_data: Multiple log entries separated by newlines
  "2026-02-03 14:30:15 ERROR Database connection failed
   2026-02-03 14:30:20 INFO User login successful
   2026-02-03 14:30:25 ERROR File not found
   2026-02-03 14:30:30 WARNING Low memory"

Tasks:
1. Split log_data by newlines to get individual entries
2. For each entry, extract timestamp, level, and message
3. Count occurrences of each log level (ERROR, INFO, WARNING)
4. Find all ERROR messages
5. Print summary statistics and all errors

Expected Output:
Log Summary
-----------
Total Entries: 4
ERROR: 2
INFO: 1
WARNING: 1

Error Messages:
1. [2026-02-03 14:30:15] Database connection failed
2. [2026-02-03 14:30:25] File not found

Hints:
- Use split('\n') for lines
- Use split() for each line
- Use counters for each level
- Store error details in lists
- Use enumerate() for numbering

Rubric:
- Correct parsing of all entries: 25%
- Correct level counting: 30%
- Correct error extraction: 25%
- Proper formatted output: 20%
"""

# Input data
log_data = """2026-02-03 14:30:15 ERROR Database connection failed
2026-02-03 14:30:20 INFO User login successful
2026-02-03 14:30:25 ERROR File not found
2026-02-03 14:30:30 WARNING Low memory"""

# Your code here
