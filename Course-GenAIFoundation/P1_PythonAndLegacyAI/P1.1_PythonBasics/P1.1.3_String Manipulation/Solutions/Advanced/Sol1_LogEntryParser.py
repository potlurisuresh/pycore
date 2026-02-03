"""
Advanced Solution 1: Log Entry Parser
"""
import re

# Input data
log_database = """2026-02-03 09:15:22 INFO Application started
2026-02-03 09:16:45 ERROR Database connection timeout
2026-02-03 09:17:10 INFO User:admin logged in from IP:192.168.1.100
2026-02-03 09:18:33 ERROR Database connection timeout
2026-02-03 09:20:15 ERROR File not found: config.xml
2026-02-03 09:25:40 INFO Processing completed: 95% success
2026-02-03 09:26:50 ERROR Database connection timeout"""

# Parse log entries
log_lines = log_database.strip().split("\n")

# Initialize lists
levels = []
messages = []
error_messages = []
error_times = []

# Process each log entry
for log in log_lines:
    parts = log.split()
    time = parts[1]
    level = parts[2]
    message = " ".join(parts[3:])
    
    levels.append(level)
    messages.append(message)
    
    if level == "ERROR":
        error_messages.append(message)
        error_times.append(time)

# Count log levels
info_count = levels.count("INFO")
error_count = levels.count("ERROR")

# Find repeated errors
repeated_errors = []
for error in error_messages:
    count = error_messages.count(error)
    if count > 1 and error not in repeated_errors:
        repeated_errors.append(error)

# Extract metadata using regex
user_pattern = r"User:(\w+)"
ip_pattern = r"IP:([\d.]+)"
pct_pattern = r"(\d+)%"

users = []
ips = []

for message in messages:
    user_match = re.search(user_pattern, message)
    if user_match:
        users.append(user_match.group(1))
    
    ip_match = re.search(ip_pattern, message)
    if ip_match:
        ips.append(ip_match.group(1))

# Calculate time interval between first and last error
if len(error_times) > 1:
    time1_parts = error_times[0].split(":")
    time2_parts = error_times[-1].split(":")
    
    min1 = int(time1_parts[0]) * 60 + int(time1_parts[1])
    min2 = int(time2_parts[0]) * 60 + int(time2_parts[1])
    
    total_interval = min2 - min1

# Print report
print("Comprehensive Log Analysis Report")
print("=" * 50)
print()

print("Summary Statistics:")
print(f"Total Entries: {len(log_lines)}")
print(f"INFO: {info_count} ({info_count * 100 // len(log_lines)}%)")
print(f"ERROR: {error_count} ({error_count * 100 // len(log_lines)}%)")
print()

print("Error Pattern Analysis:")
for error in repeated_errors:
    count = error_messages.count(error)
    print(f"WARNING: REPEATED ERROR ({count}x): {error}")
print()

print("Timeline Analysis:")
print("ERROR Events:")
for i in range(len(error_times)):
    print(f"  {error_times[i]} - {error_messages[i]}")

if len(error_times) > 1:
    print(f"\nTime span: {total_interval} minutes")
print()

print("Metadata Extraction:")
if len(users) > 0:
    print(f"Users detected: {', '.join(users)}")
if len(ips) > 0:
    print(f"IP addresses: {', '.join(ips)}")
print()

print("Recommendations:")
if len(repeated_errors) > 0:
    print(f"1. Investigate repeated errors: {repeated_errors[0]}")
if len(users) > 0:
    print(f"2. Monitor user activity: {', '.join(users)}")
