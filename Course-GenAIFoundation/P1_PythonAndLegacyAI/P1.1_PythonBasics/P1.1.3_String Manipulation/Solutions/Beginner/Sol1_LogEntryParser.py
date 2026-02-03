"""
Beginner Solution 1: Log Entry Parser
"""

# Input data
log_entry = "2026-02-03 14:30:15 ERROR Database connection failed"

# Parse the log entry by splitting on spaces
parts = log_entry.split()

# Extract components
date = parts[0]
time = parts[1]
level = parts[2]
# Message is everything after the first 3 parts
message = " ".join(parts[3:])

# Print formatted output
print("Log Entry Parser")
print("=" * 20)
print(f"Date: {date}")
print(f"Time: {time}")
print(f"Log Level: {level}")
print(f"Message: {message}")
