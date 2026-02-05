"""
Advanced Solution 1: Log Entry Parser (Concise)
"""
import re
from datetime import datetime

# Input data
log_stream = """2026-02-03 09:15:22 INFO Application started
2026-02-03 09:16:45 ERROR Database connection timeout
2026-02-03 09:17:10 INFO User:admin logged in from IP:192.168.1.100
2026-02-03 09:18:33 ERROR Database connection timeout
2026-02-03 09:20:15 ERROR File not found: config.xml
2026-02-03 09:25:40 INFO Processing completed: 95% success
2026-02-03 09:26:50 ERROR Database connection timeout"""

lines = [line.strip() for line in log_stream.strip().splitlines() if line.strip()]
records = []
for line in lines:
    parts = line.split()
    ts = " ".join(parts[:2])
    level = parts[2]
    message = " ".join(parts[3:])
    records.append((ts, level, message))

levels = [r[1] for r in records]
messages = [r[2] for r in records]
error_records = [(r[0], r[2]) for r in records if r[1] == "ERROR"]

level_counts = {lvl: levels.count(lvl) for lvl in set(levels)}
error_counts = {}
for _, msg in error_records:
    error_counts[msg] = error_counts.get(msg, 0) + 1
repeated_errors = {msg: cnt for msg, cnt in error_counts.items() if cnt > 1}

user_pattern = r"User:(\w+)"
ip_pattern = r"IP:([\d.]+)"
pct_pattern = r"(\d+)%"

users = [m.group(1) for msg in messages if (m := re.search(user_pattern, msg))]
ips = [m.group(1) for msg in messages if (m := re.search(ip_pattern, msg))]
percentages = [m.group(1) for msg in messages if (m := re.search(pct_pattern, msg))]

error_times = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts, _ in error_records]
burst_detected = False
for i in range(len(error_times) - 2):
    if (error_times[i + 2] - error_times[i]).total_seconds() <= 30:
        burst_detected = True
        break

print("Log Analysis Report")
print("=" * 48)
print(f"Total Entries: {len(records)}")
print("By Level:", ", ".join(f"{k}={v}" for k, v in sorted(level_counts.items())))

if repeated_errors:
    print("\nRepeated Errors:")
    for msg, cnt in repeated_errors.items():
        print(f"- {msg} ({cnt}x)")

if error_records:
    span_sec = int((error_times[-1] - error_times[0]).total_seconds()) if len(error_times) > 1 else 0
    print("\nError Timeline:")
    for ts, msg in error_records:
        print(f"- {ts} | {msg}")
    if span_sec:
        print(f"Time span: {span_sec}s")

print("\nExtracted Metadata:")
print(f"Users: {', '.join(users) if users else 'None'}")
print(f"IPs: {', '.join(ips) if ips else 'None'}")
print(f"Percentages: {', '.join(percentages) if percentages else 'None'}")

print("\nInsights:")
if burst_detected:
    print("- ERROR burst detected (3+ errors within 30s)")
if repeated_errors:
    top_error = max(repeated_errors, key=repeated_errors.get)
    print(f"- Investigate recurring error: {top_error}")
if users:
    print(f"- User activity observed: {', '.join(sorted(set(users)))}")
