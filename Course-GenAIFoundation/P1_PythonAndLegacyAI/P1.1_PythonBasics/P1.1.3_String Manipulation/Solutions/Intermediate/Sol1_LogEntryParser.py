"""
Intermediate Solution 1: Log Entry Parser
"""
import re

# Input data
log_data = """2026-02-03 14:30:15 INFO User logged in
2026-02-03 14:31:20 ERROR Database connection failed
2026-02-03 14:32:10 INFO Data retrieved successfully
2026-02-03 14:33:45 ERROR File not found"""

# Parse all log entries
log_lines = log_data.strip().split("\n")

# Initialize counters
info_count = 0
error_count = 0
error_messages = []

# Process each log entry
for log in log_lines:
    parts = log.split()
    level = parts[2]
    message = " ".join(parts[3:])
    
    if level == "INFO":
        info_count += 1
    elif level == "ERROR":
        error_count += 1
        error_messages.append(message)

# Print formatted output
print("Log Analysis Report")
print("=" * 30)
print(f"Total Entries: {len(log_lines)}")
print(f"INFO: {info_count}")
print(f"ERROR: {error_count}")
print()
print("Error Messages:")
for msg in error_messages:
    print(f"  - {msg}")
