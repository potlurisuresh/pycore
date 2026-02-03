"""
Beginner Assignment 1: Log Entry Parser

Scenario:
You're monitoring a simple application log file. Parse a log entry to extract
the timestamp, log level, and message.

Input:
- log_entry: "2026-02-03 14:30:15 ERROR Database connection failed"

Tasks:
1. Split the log entry by spaces to get parts
2. Extract timestamp (first 2 parts combined)
3. Extract log level (3rd part)
4. Extract message (remaining parts joined)
5. Print each component in a formatted way

Expected Output:
Timestamp: 2026-02-03 14:30:15
Level: ERROR
Message: Database connection failed

Hints:
- Use split() to break the string
- Use list indexing to access parts
- Use join() to combine message parts
- Use f-strings for output

Rubric:
- Correct splitting: 30%
- Correct extraction of timestamp: 20%
- Correct extraction of level: 20%
- Correct message reconstruction: 20%
- Proper formatted output: 10%
"""

# Input data
log_entry = "2026-02-03 14:30:15 ERROR Database connection failed"

# Your code here
